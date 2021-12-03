#!/bin/sh
sxhkd -c /usr/home/ken/.config/sxhkd/sxhkdrc &
xdotool key Num_Lock &
feh --bg-scale /home/ken/Pictures/Wallpapers/gruvbox_jocelin-carmes-giant-skeleton-barn.jpg
xsettingsd &
spotifyd &
playerctl & 
picom --experimental-backends &
