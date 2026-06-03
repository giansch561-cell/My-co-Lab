#!/bin/bash

PROJECT_DIR="/home/zerocool/My-co-Lab"

DATE_DIR=$(date +"%Y-%m-%d")

PHOTO_DIR="$PROJECT_DIR/media/photos/$DATE_DIR"

LOG="$PROJECT_DIR/data/camera_capture.log"

TIMESTAMP=$(date +"%H-%M-%S")

FILE="$PHOTO_DIR/${TIMESTAMP}.jpg"

mkdir -p "$PHOTO_DIR"

rpicam-still -o "$FILE"

if [ $? -eq 0 ]; then
echo "Photo captured: $FILE at $(date)" >> "$LOG"
echo "OK: $FILE"
else
echo "Photo capture failed at $(date)" >> "$LOG"
echo "ERROR: photo capture failed"
exit 1
fi
