# Profile file. Runs on login. Environmental variables are set here.
# I use this to run all programs once dwm starts
# Default Programs
export EDITOR="nvim"
export TERMINAL="st"
export BROWSER="brave"
export READER="zathura"

# Move dotfiles to .config folder to clean up
export ZDOTDIR="$HOME/.config/zsh"
export GTK2_RC_FILES="$HOME/.config/gtk-2.0/gtkrc-2.0"

# Path change
#export PATH="$HOME/.local/bin/"

# If user ID is greater than or equal to 1000 & if ~/bin exists and is a directory & if ~/bin is not already in your $PATH
# then export ~/.local/bin to your $PATH.
if [[ $UID -ge 1000 && -d $HOME/.local/bin && -z $(echo $PATH | grep -o $HOME/.local/bin) ]]
then
    export PATH="${PATH}:$HOME/.local/bin"
fi

xrdb -merge "$HOME/.cache/wal/colors.Xresources"
# Startup after path is set

picom -b
