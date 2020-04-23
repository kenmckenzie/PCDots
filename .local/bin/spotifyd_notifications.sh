#!/bin/sh
# Script to show notifications on song change in spotifyd,
# not really as full featured as the main app though
# dependencies are curl,xargs,cut,jq
# add onevent = "bash /home/YOU_USER/bin/spotifyNotifications.sh" to your spotifyd.conf

user_id=e442eedd888c4e17a5d11a5cf18870e0 # generated on https://developer.spotify.com/dashboard/applications
secret_id=fda7fc348ac844399597090a2a102e11

myToken=$(curl -s -X 'POST' -u $user_id:$secret_id -d grant_type=client_credentials https://accounts.spotify.com/api/token | jq '.access_token' | cut -d\" -f2)
RESULT=$?


if [ "$PLAYER_EVENT" = "start" ] || [ "$PLAYER_EVENT" = "change" ];
then
  trackName=$(playerctl metadata title)
  artistAndAlbumName=$(playerctl metadata --format "{{ artist }} ({{ album }})")

  notify-send -u low "$trackName" "$artistAndAlbumName "
fi