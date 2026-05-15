#!/bin/bash

DEVICE="/dev/$1"
MOUNT_POINT="/mnt/mycolab_usb"

SOURCE="/home/zerocool/My-co-Lab"
DEST="$MOUNT_POINT/My-co-Lab-Export"

LCD="/home/zerocool/My-co-Lab/scripts/lcd_message.sh"
LOG="/home/zerocool/My-co-Lab/data/usb_backup.log"

echo "USB detected: $DEVICE at $(date)" >> "$LOG"

# libertar /dev/ttyACM0
sudo systemctl stop mycolab-logger.service
sleep 2

$LCD "USB DETECTED" "Mounting..."
sleep 2

mkdir -p "$MOUNT_POINT"

mount "$DEVICE" "$MOUNT_POINT"

if [ $? -ne 0 ]; then
    $LCD "USB ERROR" "Mount failed"
    sudo systemctl start mycolab-logger.service
    exit 1
fi

$LCD "COPYING" "Please wait"

mkdir -p "$DEST"

rsync -rtv --no-owner --no-group --no-perms \
    "$SOURCE/data/" "$DEST/data/" \
    >> "$LOG" 2>&1

rsync -rtv --no-owner --no-group --no-perms \
    "$SOURCE/photos/" "$DEST/photos/" \
    >> "$LOG" 2>&1

rsync -rtv --no-owner --no-group --no-perms \
    "$SOURCE/videos/" "$DEST/videos/" \
    >> "$LOG" 2>&1

rsync -rtv --no-owner --no-group --no-perms \
    --exclude "environment/" \
    "$SOURCE/timelapse/" "$DEST/timelapse/" \
    >> "$LOG" 2>&1

sync

$LCD "CLEANING" "Local data"

find "$SOURCE/data/environment" \
-type f \
-name "*.csv" \
-delete

sleep 2

$LCD "UNMOUNTING" "Please wait"

umount "$MOUNT_POINT"

$LCD "BACKUP DONE" "Remove USB"

sleep 5

sudo -u zerocool -H python3 -m mpremote connect /dev/ttyACM0 reset

sleep 5

sudo systemctl start mycolab-logger.service
