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
# and http://superuser.com/a/734410/250287
shopt -s histappend
# value from /etc/bashrc on Fedora 25
#export PROMPT_COMMAND='printf "\033k%s@%s:%s\033\\" "${USER}" "${HOSTNAME%%.*}" "${PWD/#$HOME/\~}"'
# ...this preserves the PROMPT_COMMAND...
#export PROMPT_COMMAND="${PROMPT_COMMAND:+$PROMPT_COMMAND$'\n'}history -a; history -c; history -r"
# ...but we don't want that:
export PROMPT_COMMAND="history -a; history -c; history -r"
# this will change it to 'PROMPT_HERE':
# printf '\ekPROMPT_HERE\e\\'
export IGNOREEOF=1

export PATH=$HOME/.local/bin:$PATH
export PATH=$HOME/bin:$PATH

alias ls="ls --color -F"
alias rm="rm -i"
alias mv="mv -i"
alias cp="cp -i"

alias psc='ps xawf -eo pid,user,cgroup,args'

alias start=xdg-open

# from http://www.catonmat.net/blog/git-aliases
# also see:
#   http://www.robo47.net/blog/208-Git-Aliases-Submodules-and-Symfony
#   http://blogs.gnome.org/danni/2011/03/07/useful-git-aliases/
#   http://volnitsky.com/project/git-prompt
alias ga='git add'
alias gd='git diff --stat'
alias gl="git log --oneline --graph --date-order --decorate --pretty=format:'%Creset %Cgreen%h %Creset%C(bold white) %s %C(bold black)by%C(reset) %C(cyan)%an%Creset (%ar) %C(yellow) %d %Cred %ad' --branches"
alias ggg=gl
alias gg='gl --color=always | head -50'
alias g='gl --color=always | head -10'
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


# Set SSH to use gpg-agent  -- from https://wiki.archlinux.org/index.php/GnuPG#Unattended_passphrase
# Set GPG TTY
export GPG_TTY=$(tty)
unset SSH_AGENT_PID
if [ "${gnupg_SSH_AUTH_SOCK_by:-0}" -ne $$ ]; then
    export SSH_AUTH_SOCK="/run/user/$UID/gnupg/S.gpg-agent.ssh"
else
    # Refresh gpg-agent tty in case user switches into an X session
    gpg-connect-agent updatestartuptty /bye >/dev/null
fi


# from https://eklitzke.org/using-ssh-agent-and-ed25519-keys-on-gnome
# from https://ask.fedoraproject.org/en/question/92448/how-do-i-get-proper-ssh-agent-functionality-in-gnome/
# mkdir -p ~/.config/systemd/user
# cat > ~/.config/systemd/user/ssh-agent.service <<EOF
# [Unit]
# Description=OpenSSH private key agent
# IgnoreOnIsolate=true
# 
# [Service]
# Type=forking
# Environment=SSH_AUTH_SOCK=%t/ssh-agent.socket
# ExecStart=/usr/bin/ssh-agent -a $SSH_AUTH_SOCK
# #ExecStartPost=/usr/bin/systemctl --user set-environment SSH_AUTH_SOCK=${SSH_AUTH_SOCK}
# ExecStartPost=/usr/bin/systemctl --user set-environment SSH_AUTH_SOCK=${SSH_AUTH_SOCK} GSM_SKIP_SSH_AGENT_WORKAROUND="true"
# 
# [Install]
# WantedBy=default.target
# 
# EOF
# systemctl --user enable ssh-agent.service
#
# Probably don't need this, but may need to add this to .bashrc just in case:
# systemctl --user import-environment SSH_AUTH_SOCK

if [ -e .bashrc.d/`hostname` ] ; then
  . .bashrc.d/`hostname`
fi



export EDITOR=~/bin/editor

export PYTHONSTARTUP=~/.pythonrc
export PYTHONIOENCODING=utf-8

# Prompts:
## basic
# export PS1='\[\033[1;34m\](\A) \W \$ \[\033[m\]'
## a nice `root` one, with bright red background
#export PS1='\[\033[41;1;37m\]\D{%Y%m%d-%H:%M.%S} \u\[\033[0m\]\[\033[1;37m\]@\[\033[1;33m\]\h\[\033[1;36m\] \[\033[1;31m\]\W\[\033[m\] \[\033[1;34m\]▶\[\033[m\] \$ \[\033[m\]'
# normal user
export PS1='\[\033[1;34m\]\D{%Y%m%d-%H:%M.%S}\[\033[0m\] \[\033[1;34m\]\u\[\033[1;37m\]@\[\033[1;33m\]\h\[\033[1;36m\] \[\033[1;31m\]\W\[\033[m\] \[\033[1;34m\]▶\[\033[m\] \$ \[\033[m\]'


# Auto-tmux invocation. From screen instructions at
# http://taint.org/wk/RemoteLoginAutoScreen
if [ "$TERM" != "dumb" -a "$TERM" != "cygwin" -a "$PS1" != "" -a "${STARTED_SCREEN:-x}" = x -a -z "$TMUX" -a -x ~/bin/tmx -a -n "$(type -p tmux)" ]
then
  STARTED_SCREEN=1 ; export STARTED_SCREEN
  TERM=xterm-256color ~/bin/tmx ${HOSTNAME:-$(hostname)} || echo "tmux finished. continuing with normal bash startup"
fi
# [end of auto-screen snippet]
