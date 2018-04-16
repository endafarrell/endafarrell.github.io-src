title: Git branch, status and colour in your prompt guide
date: 2018-04-16
tags: unix, work, git

I use git via the ``terminal`` and not through UI tools (though I do use ``Sourcetree`` to understands the flow of 
commits), and I recently found a very helpful change for my prompt:

 ![PS1](../../../images/2018/master%20with%20uncommitted%20changes.png)
 
It's turned out to be really helpful and not difficult to set up. All of the changes are in my ``.profile``:

    COLOR_RED="\033[0;31m"
    COLOR_YELLOW="\033[0;33m"
    COLOR_GREEN="\033[0;32m"
    COLOR_OCHRE="\033[38;5;95m"
    COLOR_BLUE="\033[0;34m"
    COLOR_WHITE="\033[0;37m"
    COLOR_RESET="\033[0m"
    
    function parse_git_branch {
         git branch 2> /dev/null | sed -e '/^[^*]/d' -e 's/* \(.*\)/\1/'
    }
    
    function git_color {
      local git_status="$(git status 2> /dev/null)"
    
      if [[ ! $git_status =~ "working tree clean" ]]
      then
        echo -e $COLOR_RED
      elif [[ $git_status =~ "Your branch is ahead of" ]]
      then
        echo -e $COLOR_YELLOW
      elif [[ $git_status =~ "nothing to commit" ]]
      then
        echo -e $COLOR_GREEN
      else
        echo -e $COLOR_OCHRE
      fi
    }
    
    
    PS1="\[$COLOR_WHITE\]\W "                             # basename of pwd
    PS1+="\[\$(git_color)\]/"                             # colors git status, adds /
    PS1+="\$(vcprompt --format "%b%m%a%u" --no-newline)"  # the plus/question
    PS1+="/\[$COLOR_BLUE\]\$\[$COLOR_RESET\] "            # / then '#' for root, else '$'
    export PS1
     
This code has been a cobbling-together of other people's code - none of it is originally mine.
 
The ``vcprompt`` command is another on-my-path script - and it adds the star and question mark when there are changed 
and untracked files - which originally came from [github.com/djl/vcprompt](https://github.com/djl/vcprompt) :-)

