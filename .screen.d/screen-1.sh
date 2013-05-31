#!/bin/sh
rm -rf ~/.emacs.desktop.lock
TERM=xterm-256color EMACS_LOAD_LIBS=1 emacs -nw
