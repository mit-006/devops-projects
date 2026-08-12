#!/bin/bash

if [ -z "$1" ] || [ -z "$2" ]; then
    echo "Usage: ./backup.sh <source_dir> <destination_dir>"
    exit 1
fi


src=$1
dest=$2

mkdir -p "$dest"

log_file="/home/ubuntu/backups/backup.log"
timestamp=$(date +%Y-%m-%d_%H-%M-%S)

backup_file_name="$dest/backup_${timestamp}.tar.gz"

tar -czf "$backup_file_name" -C "$src" 

if [ $? -eq 0 ]; then
    echo "[$timestamp] Backup successful: $backup_file_name" >> "$log_file"
else
    echo "[$timestamp] Backup FAILED" >> "$log_file"
fi

find "$dest" -type f -name "backup_*.tar.gz" -mtime +7 -delete
