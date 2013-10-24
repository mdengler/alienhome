# .bashrc

# User specific aliases and functions

# Source global definitions
if [ -f /etc/bashrc ]; then
	. /etc/bashrc
fi

# from http://codeinthehole.com/archives/17-The-most-important-command-line-tip-incremental-history-searching-with-.inputrc.html
export HISTSIZE=1000000
export HISTFILESIZE=1000000000

# from http://www.ukuug.org/events/linux2003/papers/bash_tips/
shopt -s histappend
PROMPT_COMMAND='history -a'
export IGNOREEOF=1

export GREP_OPTIONS='--color=auto'

export PATH=$HOME/.local/bin:$PATH
export PATH=$HOME/bin:$PATH

alias ls="ls --color -F"
alias rm="rm -i"
alias mv="mv -i"
alias cp="cp -i"

alias psc='ps xawf -eo pid,user,cgroup,args'

# from http://www.catonmat.net/blog/git-aliases
# also see:
#   http://www.robo47.net/blog/208-Git-Aliases-Submodules-and-Symfony
#   http://blogs.gnome.org/danni/2011/03/07/useful-git-aliases/
#   http://volnitsky.com/project/git-prompt
alias ga='git add'
alias gd='git diff --stat'
#alias gl='git log --oneline --graph --date-order --decorate --pretty=format:"%Creset %Cgreen%h %Creset%C(bold white) %s %C(bold black)by%C(reset) %C(cyan)%an%Creset (%ar) %C(yellow) %d %Cred %ad" --branches'
alias gl='git log --oneline --graph --date-order --decorate --pretty=format:"%Creset %C(bold black)%h %C(reset)%C(cyan)%x1b[s%an%x1b[u%x1b[8C%Creset%C(bold white) %s %Cgreen(%ar)%C(yellow)%d %C(red)%ad" --branches'
alias glh='gl | head -28'
alias gm='git commit -m'
alias gs='git status'

# apply default git completion to custom aliases
complete -o bashdefault -o default -o nospace -F _git_add ga
complete -o bashdefault -o default -o nospace -F _git_branch gb
complete -o bashdefault -o default -o nospace -F _git_checkout gc
complete -o bashdefault -o default -o nospace -F _git_clone gcl
complete -o bashdefault -o default -o nospace -F _git_diff gd
complete -o bashdefault -o default -o nospace -F _git_log gl
complete -o bashdefault -o default -o nospace -F _git_commit gm gma
complete -o bashdefault -o default -o nospace -F _git_push gp
complete -o bashdefault -o default -o nospace -F _git_pull gpu
complete -o bashdefault -o default -o nospace -F _git_remote gra grr


# from http://tychoish.com/rhizome/9-awesome-ssh-tricks/
ssh-reagent () {
        for agent in /tmp/ssh-*/agent.*; do
               export SSH_AUTH_SOCK=$agent
               if ssh-add -l 2>&1 > /dev/null; then
                       echo Found working SSH Agent:
                       ssh-add -l
                       return
               fi
       done
       echo Cannot find ssh agent - maybe you should reconnect and forward it?
}


if [ -e .bashrc.d/`hostname` ] ; then
  . .bashrc.d/`hostname`
fi



export EDITOR=~/bin/editor

export PYTHONSTARTUP=~/.pythonrc


# Auto-tmux invocation. From screen instructions at
# http://taint.org/wk/RemoteLoginAutoScreen
if [ "$TERM" != "dumb" -a "$TERM" != "cygwin" -a "$PS1" != "" -a "${STARTED_SCREEN:-x}" = x -a -z "$TMUX" ]
then
  STARTED_SCREEN=1 ; export STARTED_SCREEN
  TERM=xterm-256color ~/bin/tmx ${HOSTNAME:-$(hostname)} || echo "tmux finished. continuing with normal bash startup"
fi
# [end of auto-screen snippet]

