#!/bin/sh
trap 'trap - SIGTERM && kill -- -$$' SIGINT SIGTERM EXIT
sudo true
mkfifo /tmp/zalman_temp_display.fifo
sudo ./zalman_temp_display.py < /tmp/zalman_temp_display.fifo &
while true; do sensors 2> /dev/null | grep Tctl | grep -o -P '(?<=\+)[0-9]+' > /tmp/zalman_temp_display.fifo; sleep 1; done