#!/bin/sh
xbindkeys &
killall pulseaudio &
pulseaudio &
spotify-qt &
sh empty_trash.sh &