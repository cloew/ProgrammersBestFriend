_pbf_completion()
{
    local cur=${COMP_WORDS[COMP_CWORD]}
    
    unset COMP_WORDS[${#COMP_WORDS[@]}-1]
    unset COMP_WORDS[0]
    
    SAVE_IFS=$IFS
    IFS=" "
    COMP_JOIN="${COMP_WORDS[*]}"
    IFS=$SAVE_IFS
    text=`pbf -c $COMP_JOIN`
    
    if [ -n "$text" ]; then
        COMPREPLY=( $(compgen -W "$text" -- $cur) )
    else
        COMPREPLY=( $(compgen -f -- $cur) )
    fi
    }
complete -d -F _pbf_completion pbf