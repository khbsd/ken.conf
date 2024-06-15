# current time with milliseconds
current_time() {
    echo "%*"
}

username() {
    echo "%{$fg[cyan]%}%n%{$reset_color%}"
}

home_dir() {
    echo "%{$fg[blue]%}%~%{$reset_color%}"
}

# returns if there are errors, nothing otherwise
return_status() {
    echo "%(?..%{$fg[red]%}%B$(icon_negate) %b%{$return_status%}%{$fg[magenta]%}oof%{$reset_color%}%{$fg[red]%}!%{$reset_color%})"
}

icon_git() {
    echo "\Ue702"
}

icon_arch() {
    echo "\Uf08c7"
}

icon_negate() {
    echo "¬"
}

icon_therefore() {
    echo "∴"
}

icon_doublearrow() {
    echo "»"
}

PROMPT="%{$fg[cyan]%}%B $(icon_arch) %b$(username)%{$reset_color%}:$(home_dir)%{$fg[yellow]%} $(icon_git) $(git_current_user_name)%{$reset_color%}:%{$fg[blue]%}$(git_prompt_info)%{$reset_color%} "
RPROMPT="%{$fg[red]%}%B$(icon_therefore) %b%{$reset_color%}%{$fg[blue]%}$(current_time)%{$reset_color%} %{$fg[green]%}%B$(icon_doublearrow)%b%{$reset_color%} %{$fg[magenta]%}$(return_status)%{$reset_color%}"

ZSH_THEME_GIT_PROMPT_PREFIX="%{$fg[green]%}"
ZSH_THEME_GIT_PROMPT_SUFFIX="%{$reset_color%} "
