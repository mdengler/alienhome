#!/bin/bash
#set -x
set -e

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
ROOT=$(readlink -f "${DIR}/..")
cd "${ROOT}"

timestamp="$(date +%Y%m%d%H%M%S)"
YYYYMMDD="${timestamp:0:8}"


# copy alienhome content, with backups (don't use rsync because we don't want all attrs preserved)
a-copy () {
    target="${HOME}/${1}"
    source="${1}"
    [ -e "$target" ] && mv "${target}" "${target}.bak-${timestamp}"
    echo cp -a "${source}" "${target}"
    cp -a "${source}" "${target}"
}

# link to alienhome content, with backups
a-link () {
    target="${HOME}/${1}"
    source="${ROOT}/${1}"
    [ -e "$target" ] && mv "${target}" "${target}.bak-${timestamp}"
    echo ln -s "${source}" "${target}"
    ln -s "${source}" "${target}"
}


# replace xdg / freedesktop.org dirs with links to mine
a-link-xdg () {
    xdg="${HOME}/{1}"
    mine="${HOME}/${2}"
    if [ -d "${xdg}" ] ; then
	mv "${xdg}" "${xdg}.bak-${timestamp}"
	echo ln -s "${mine}" "${xdg}"
	ln -s "${mine}" "${xdg}"
    fi
}


# link homedir files / dotfiles
for f in $(find . -maxdepth 1 -type f) ; do
    if ! echo "${f}" | grep -q alienhome ; then
	a-link $f
    fi
done


# link subdir contents
for f in $(find . -maxdepth 2 -type f) ; do
    mkdir -p "${HOME}/$(dirname ${f})"
    a-link "${f}"
done


# dir structure
[ ! -e "${HOME}/.git" ] && ( cd "${HOME}" && git init )
mkdir -p "${HOME}/bin"
mkdir -p "${HOME}/etc/av"
mkdir -p "${HOME}/src"
mkdir -p "${HOME}/tmp"

a-link-xdg Documents doc
a-link-xdg Downloads tmp
a-link-xdg Pictures etc/av
a-link-xdg Public doc/public_html/martindengler.com
a-link-xdg Templates tmp
a-link-xdg Videos etc/av



# special steps
## .emacs expects ~/.emacs.d/site-lisp
mkdir -p "${HOME}/.emacs.d/site-lisp"


