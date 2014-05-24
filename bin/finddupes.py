#!/usr/bin/env python
"""%prog - find duplicate files in one or more directory trees

Examples:

finddupes.py .
finddupes.py . /some/other/dir
finddupes.py --exclude-extensions=txt,csv --only-shallowest-dupes .
find . -type f -print0 | xargs -0 sha1sum | finddupes.py --shasum-input

finddupes.py --include-extensions=jpg \
  --exclude-shallowest-dupes --only-filenames --null . \
  | xargs -0 rm

prints out the SHA hash and filenames of all files below the
directories specified on the command line if two or more files have
the same SHA hash

Alternately, passing --show-dedupe will cause primitive de-dupe commands to be
printed (not run).


Alternates: Similar in purpose to rdfind ( http://rdfind.pauldreik.se/ ) and
duff ( http://duff.dreda.org/ ), but written before I found them and more
scriptable.

TODO:

- ignore zero-length files
- optimize away the need to hash files if --only-filenames is passed
- ignore small files

"""

import os
import sha
import sys

from optparse import OptionParser



def hash_onefile(absfname, hashes):
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


def hash_dirs(dirnames, exclude_extensions=(), include_extensions=(), hashes=None):
    if hashes is None:
        hashes = {}

    def hash_onedir_wrapped(*args, **kwargs):
        hash_onedir(*args, hashes=hashes, **kwargs)

    for dirname in dirnames:
        os.path.walk(dirname,
                     hash_onedir_wrapped,
                     (exclude_extensions, include_extensions))

    return hashes


def finddupes(hashes, only_shallowest_dupes=False):
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


def report_dupes(dupes,
                 outfh=None,
                 only_filenames=False,
                 exclude_earliest=False,
                 exclude_shallowest=False,
                 null_delimiters=False,
                 show_dedupe=False):

    if exclude_earliest and exclude_shallowest:
        msg = "both exclude_earliest (--exclude-earliest) and" \
              " exclude_shallowest (--exclude_shallowest) cannot be True"
        raise ValueError(msg)

    if show_dedupe and (not any((exclude_earliest, exclude_shallowest))):
        msg = "one of exclude_earliest (--exclude-earliest) or" \
              " exclude_shallowest (--exclude-shallowest) must be True " \
              " when show_dedupe (--show-dedupe) is True"
        raise ValueError(msg)

    if show_dedupe and only_filenames:
        raise ValueError("both show_dedupe and only_filenames cannot be True")

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

        original = None

        if exclude_shallowest:
            sorted_fnames = sorted(fnames)
            original = sorted_fnames.pop(0)

        elif exclude_earliest:
            sorted_fnames = sorted(fnames, _by_lastmod_time_by_name_rev)
            original = sorted_fnames.pop(0)

        else:
            sorted_fnames = sorted(fnames, _by_lastmod_time_by_name_rev)

        delimiter = "\n" if not null_delimiters else chr(0)

        for fname in sorted_fnames:
            if show_dedupe:
                outfh.write("rm '%s' && ln '%s' '%s'%s" % (fname, original, fname, delimiter))
            elif only_filenames:
                outfh.write("%s%s" % (fname, delimiter))
            else:
                outfh.write("%s,%s%s" % (dupehash, fname, delimiter))


def finddupes_in_dirs(dirnames,
                      only_shallowest_dupes=False,
                      exclude_extensions=(),
                      include_extensions=(),
                      hashes=None):
    """utility function for interactive / library use"""

    hashes = hash_dirs(dirnames,
                       exclude_extensions,
                       include_extensions,
                       hashes=hashes)

    dupes = finddupes(hashes,
                      only_shallowest_dupes=only_shallowest_dupes)

    return dupes, hashes


def finduniques(hashes):
    return dict((h, v) for h, v in hashes.iteritems() if len(v) < 2)


def report_uniques(uniques,
                   outfh=None,
                   only_filenames=False,
                   sort_by_hash=False,
                   null_delimiters=False):
    """writes lines of uniques to outfh

    sort order is by filename by default (use sort_by_hash=True to sort by hash)

    """
    outfh = outfh or sys.stdout
    if sort_by_hash:
        items_sorted = sorted(uniques.iteritems())
    else:
        items_sorted = sorted(uniques.iteritems(), cmp=lambda p1, p2: cmp(p1[1], p2[1]))
    if only_filenames:
        lines = (fname for hash_, fname in items_sorted)
    else:
        lines = ("{},{}".format(hash, fname) for hash, (fname, ) in items_sorted)
    delimiter = "\n" if not null_delimiters else chr(0)
    outfh.write(delimiter.join(lines))


def finduniques_in_dirs(dirnames,
                        exclude_extensions=(),
                        include_extensions=(),
                        hashes=None):
    """utility function for interactive / library use"""

    hashes = hash_dirs(dirnames,
                       exclude_extensions,
                       include_extensions,
                       hashes=hashes)

    uniques = finduniques(hashes)

    return uniques, hashes


def main_get_hashes(options, args):

    hashes = {}

    dirnames = []
    filenames = []

    if options.shasum_input:
        for line in sys.stdin.readlines():
            line = line.strip()
            filehash = line.split()[0]
            fname = line[len(filehash):].strip()  # XXX: whitespace issue?
            if filehash not in hashes:
                hashes[filehash] = []
            hashes[filehash].append(fname)

    elif len(args) == 0:
        for fname in sys.stdin.readlines():
            fname = fname.strip()
            if os.path.isdir(fname):
                dirnames.append(fname)
            else:
                filenames.append(fname)
    else:
        dirnames.extend(args)

    for filename in filenames:
        hash_onefile(filename, hashes=hashes)

    hash_dirs(dirnames,
              exclude_extensions=options.exclude_extensions,
              include_extensions=options.include_extensions,
              hashes=hashes)

    return hashes


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
                      " --only-filenames (e.g., to find list of later dupes"
                      " to delete)")
    parser.add_option("-X", "--exclude-shallowest-dupe",
                      action="store_true",
                      help="when reporting dupes, skip shallowest"
                      " (it will not be printed).  Useful with"
                      " --only-filenames (e.g., to find list of deeper dupes"
                      " to delete)")
    parser.add_option("-F", "--only-filenames", action="store_true",
                      help="only report filenames, not hashes"
                      " (useful with --exclude-earliest-dupe)")
    parser.add_option("-u", "-U", "--unique", action="store_true",
                      help="invert function: only report unique hashes & files")
    parser.add_option("-0", "--null", action="store_true",
                      help="output is null-delimited.  Useful with"
                      " --only-filesnames")
    parser.add_option("-D", "--show-dedupe", action="store_true",
                      help="show commands to dedupe (using hard links) files"
                      " instead of the normal output")
    parser.set_usage(__doc__)
    options, args = parser.parse_args()

    hashes = main_get_hashes(options, args)

    if options.unique:
        uniques = finduniques(hashes)

        report_uniques(uniques,
                       only_filenames=options.only_filenames,
                       null_delimiters=options.null)

    else:

        dupes = finddupes(hashes,
                          only_shallowest_dupes=options.only_shallowest_dupes)

        report_dupes(dupes,
                     only_filenames=options.only_filenames,
                     exclude_earliest=options.exclude_earliest_dupe,
                     exclude_shallowest=options.exclude_shallowest_dupe,
                     null_delimiters=options.null,
                     show_dedupe=options.show_dedupe)
