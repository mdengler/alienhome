#!/usr/bin/env python
"""

%prog - find duplicate files in one or more directory trees

Examples:

finddupes.py .
finddupes.py . /some/other/dir
finddupes.py --exclude-extensions=txt,csv --only-shallowest-dupes .
find . -type f -print0 | xargs -0 sha1sum | finddupes.py --shasum-input

prints out the SHA hash and filenames of all files below the
directories specified on the command line if two or more files have
the same SHA hash
"""

import os
import sha
import sys

from optparse import OptionParser



_hashes = {}
def hash_onefile(absfname, hashes=None):
    if hashes is None:
        hashes = _hashes
    filehash = sha.sha(open(absfname).read()).hexdigest()
    if filehash not in hashes:
        hashes[filehash] = []
    hashes[filehash].append(absfname)
    return filehash


def hash_onedir((exclude_extensions, include_extensions),
                dirname,
                fnames,
                hashes=None):
    for fname in fnames:
        absfname = os.path.join(dirname, fname)
        if (not os.path.isdir(absfname)) and os.path.exists(absfname):
            if ((include_extensions is not None)
                or
                (exclude_extensions is not None)):
                extension = os.path.splitext(absfname)[-1][1:]
                if exclude_extensions:
                    if extension in exclude_extensions.split(","):
                        continue
                if include_extensions:
                    if extension not in include_extensions.split(","):
                        continue
            hash_onefile(absfname, hashes=hashes)


def finddupes(hashes, only_shallowest_dupes=False, exclude_extensions=None, include_extensions=None):
    dupes = dict((h, v) for h, v in hashes.iteritems() if len(v) > 1)

    if only_shallowest_dupes:
        shallowest_dupes = {}
        for dupehash in dupes:
            dirlens = {}
            for fname in hashes[dupehash]:
                dirname, basename = os.path.split(fname)
                depth = len(dirname.split(os.path.sep)) #XXX: whitespace issue?
                if depth not in dirlens:
                    dirlens[depth] = []
                dirlens[depth].append(fname)
            if len(dirlens) > 1:
                shallowest_dupes[dupehash] = sum(
                    [dirlens[d] for d in sorted(dirlens.keys())[:-1]],
                    [])
            else:
                shallowest_dupes[dupehash] = hashes[dupehash]
        dupes = shallowest_dupes

    return dupes


def report_dupes(dupes, outfh=None, only_filenames=False, exclude_earliest=False):
    if outfh is None:
        outfh = sys.stdout

    def _by_lastmod_time(fname_a, fname_b):
        return cmp(os.stat(fname_a).st_mtime,
                   os.stat(fname_b).st_mtime)

    def _by_lastmod_time_by_name_rev(fname_a, fname_b):
        bytime = _by_lastmod_time(fname_a, fname_b)
        if bytime != 0:
            return bytime
        return -1 * cmp(fname_a, fname_b)

    for dupehash, fnames in dupes.iteritems():
        sorted_fnames = sorted(fnames, _by_lastmod_time_by_name_rev)
        if exclude_earliest:
            sorted_fnames.pop(0)
        for fname in sorted_fnames:
            if only_filenames:
                outfh.write("%s\n" % fname)
            else:
                outfh.write("%s,%s\n" % (dupehash, fname))


def finddupes_in_dirs(dirnames,
                      only_shallowest_dupes=False,
                      exclude_extensions=(),
                      include_extensions=(),
                      hashes=None):
    if hashes is None:
        hashes = {}

    def hash_onedir_wrapped(*args, **kwargs):
        hash_onedir(*args, hashes=hashes, **kwargs)

    for dirname in dirnames:
        os.path.walk(dirname,
                     hash_onedir_wrapped,
                     (exclude_extensions,
                      include_extensions))

    dupes = finddupes(hashes,
                      only_shallowest_dupes=only_shallowest_dupes,
                      exclude_extensions=exclude_extensions,
                      include_extensions=include_extensions)

    return dupes, hashes



if __name__ == "__main__":
    parser = OptionParser()
    parser.add_option("--only-shallowest-dupes", action="store_true",
                      help="only report names of the shallowest"
                      " (in directory tree) duplicated")
    parser.add_option("--exclude-extensions",
                      help="comma-separated list of extensions"
                      " (no dots) to exclude from even being considered"
                      " as possibly duplicated (takes precedence over"
                      " --include-extensions)")
    parser.add_option("--include-extensions",
                      help="comma-separated list of extensions (no dots)"
                      " to include from being considered as possibly"
                      " duplicated (potentially overridden by"
                      " --exclude-extensions)")
    parser.add_option("-S", "--shasum-input", action="store_true",
                      help="shasum output is being fed into stdin")
    parser.add_option("-E", "--exclude-earliest-dupe",
                      action="store_true",
                      help="when reporting dupes, skip earliest"
                      " (it will not be printed).  Useful with"
                      " --only-filenames")
    parser.add_option("-F", "--only-filenames", action="store_true",
                      help="only report filenames, not hashes"
                      " (useful with --do-not-report-earliest-of-dupes)")
    parser.set_usage(__doc__)
    options, args = parser.parse_args()

    if options.shasum_input:
        for line in sys.stdin.readlines():
            line = line.strip()
            filehash = line.split()[0]
            fname = line[len(filehash):].strip()  # XXX: whitespace issue?
            if filehash not in _hashes:
                _hashes[filehash] = []
            _hashes[filehash].append(fname)

    elif len(args) == 0:
        for fname in sys.stdin.readlines():
            fname = fname.strip()
            if os.path.isdir(fname):
                os.path.walk(fname,
                             hash_onedir,
                             (options.exclude_extensions,
                              options.include_extensions))
            else:
                hash_onefile(fname)
    else:
        for dirname in args:
            os.path.walk(dirname,
                         hash_onedir,
                         (options.exclude_extensions,
                          options.include_extensions))

    dupes = finddupes(_hashes,
                      only_shallowest_dupes=options.only_shallowest_dupes,
                      exclude_extensions=options.exclude_extensions,
                      include_extensions=options.include_extensions)

    report_dupes(dupes,
                 only_filenames=options.only_filenames,
                 exclude_earliest=options.exclude_earliest_dupe)
