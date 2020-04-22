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
export GNUPGHOME="$XDG_DATA_HOME"/gnupg
export XDG_CACHE_HOME="$HOME"/.cache
export XDG_CONFIG_HOME="$HOME"/.config
export XDG_DATA_HOME="$HOME"/.local/share

alias wget="wget --hsts-file=$XDG_CACHE_HOME/wget-hsts"

# Define XDG defaults for cleaner dotfiles for apps that support the standard
export BUNDLE_USER_CACHE="$XDG_CACHE_HOME"/bundle
export BUNDLE_USER_CONFIG="$XDG_CONFIG_HOME"/bundle
export BUNDLE_USER_PLUGIN="$XDG_DATA_HOME"/bundle
export CARGO_HOME="$XDG_DATA_HOME"/cargo
export ELINKS_CONFDIR="$XDG_CONFIG_HOME"/elinks
export GNUPGHOME="$XDG_DATA_HOME"/gnupg
...
# Path change
#export PATH="$HOME/.local/bin/"

# If user ID is greater than or equal to 1000 & if ~/bin exists and is a directory & if ~/bin is not already in your $PATH
# then export ~/.local/bin to your $PATH.
if [[ $UID -ge 1000 && -d $HOME/.local/bin && -z $(echo $PATH | grep -o $HOME/.local/bin) ]]
then
    export PATH="${PATH}:$HOME/.local/bin"
fi

# Merge xresources with wal colors so bar is themed on startup
xrdb -merge "$HOME/.cache/wal/colors.Xresources"

# Startup after path is set
picom -b
