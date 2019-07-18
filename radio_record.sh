#!/bin/sh

# CBS 음악FM
mplayer mms://media.biointernet.com/fm1021 -dumpstream -dumpfile `date +%Y%m%d%H%M`.mp3 &
sleep 7200
kill $!
