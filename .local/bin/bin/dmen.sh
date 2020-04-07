#!/bin/sh
# A script to apply colours to dmenu without having to change source,


# Import the colors
. "${HOME}/.cache/wal/colors.sh"

dmenu_run -b -nb "$color0" -nf "$color15" -sb "$color1" -sf "$color15" -fn "Hack Nerd Font Mono:pixelsize=20"
