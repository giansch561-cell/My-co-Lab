#!/bin/bash

DEVICE="/dev/$1"
MOUNT_POINT="/mnt/mycolab_usb"

SOURCE="/home/zerocool/My-co-Lab"
DEST="$MOUNT_POINT/My-co-Lab-Export"

LOG="$SOURCE/data/usb_backup.log"
SERIAL="/dev/ttyACM0"

lcd_msg() {
    printf "LCD:%s\n" "$1" > "$SERIAL" 2>/dev/null || true
    sleep 1
}

finish_logger() {
    systemctl start mycolab-logger.service
}

echo "USB detected: $DEVICE at $(date)" >> "$LOG"

systemctl stop mycolab-logger.service
sleep 1

lcd_msg "USB DETECTED"

mkdir -p "$MOUNT_POINT"

if ! mountpoint -q "$MOUNT_POINT"; then
    mount -o uid=1000,gid=1000,umask=0002 "$DEVICE" "$MOUNT_POINT"

    if [ $? -ne 0 ]; then
        lcd_msg "USB MOUNT ERROR"
        echo "Mount failed: $DEVICE at $(date)" >> "$LOG"
        finish_logger
        exit 1
    fi
fi

lcd_msg "BACKUP START"

mkdir -p "$DEST/data/environment"
mkdir -p "$DEST/photos"
mkdir -p "$DEST/videos"
mkdir -p "$DEST/docs"

rsync -rtv --no-owner --no-group --no-perms "$SOURCE/data/environment/" "$DEST/data/environment/" >> "$LOG" 2>&1
RSYNC_ENV=$?

rsync -rtv --no-owner --no-group --no-perms "$SOURCE/media/photos/" "$DEST/photos/" >> "$LOG" 2>&1
RSYNC_PHOTOS=$?

rsync -rtv --no-owner --no-group --no-perms "$SOURCE/media/videos/" "$DEST/videos/" >> "$LOG" 2>&1
RSYNC_VIDEOS=$?

rsync -rtv --no-owner --no-group --no-perms "$SOURCE/docs/" "$DEST/docs/" >> "$LOG" 2>&1
RSYNC_DOCS=$?

if [ "$RSYNC_ENV" -eq 0 ] && [ "$RSYNC_PHOTOS" -eq 0 ] && [ "$RSYNC_VIDEOS" -eq 0 ] && [ "$RSYNC_DOCS" -eq 0 ]; then
    lcd_msg "CLEANING"

    find "$SOURCE/data/environment" -type f -name "*.csv" -delete
    find "$SOURCE/media/videos" -type f -name "*.mp4" -delete

    find "$SOURCE/media/photos" -type f -name "*.jpg" -mtime +7 -delete
    find "$SOURCE/media/photos" -type f -name "*.jpeg" -mtime +7 -delete
    find "$SOURCE/media/photos" -type f -name "*.png" -mtime +7 -delete

    echo "Source files cleaned after successful backup: $(date)" >> "$LOG"
else
    lcd_msg "BACKUP ERROR"
    echo "Backup failed, source files NOT deleted: $(date)" >> "$LOG"
    echo "RSYNC_ENV=$RSYNC_ENV RSYNC_PHOTOS=$RSYNC_PHOTOS RSYNC_VIDEOS=$RSYNC_VIDEOS RSYNC_DOCS=$RSYNC_DOCS" >> "$LOG"
    finish_logger
    exit 1
fi

sync

lcd_msg "BACKUP OK"
sleep 3

umount "$MOUNT_POINT"

if [ $? -eq 0 ]; then
    lcd_msg "USB SAFE REMOVE"
    sleep 5
    printf "LCD_RESET\n" > "$SERIAL" 2>/dev/null || true
    echo "USB backup completed: $DEVICE at $(date)" >> "$LOG"
    finish_logger
else
    lcd_msg "UNMOUNT ERROR"
    echo "Unmount failed: $DEVICE at $(date)" >> "$LOG"
    finish_logger
    exit 1
fi