#!/bin/bash

LINE1="$1"
LINE2="$2"

CODE="from grove_lcd import setText
setText('${LINE1}\n${LINE2}')"

sudo -u zerocool -H python3 -m mpremote connect /dev/ttyACM0 exec "$CODE"
