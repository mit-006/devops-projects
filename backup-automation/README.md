# Automated Backup Script

A bash script that backs up a directory, compresses it with a timestamp, logs success/failure, and automatically deletes backups older than 7 days.

## Features
- Directory backup with timestamped `.tar.gz` naming
- Success/failure logging with timestamps
- Automatic rotation — deletes backups older than 7 days
- Takes source and destination as arguments

## Usage
```bash
chmod +x backup.sh
./backup.sh <source_directory> <destination_directory>
```

## Tools Used
- `tar` — compression
- `date` — timestamping
- `find` — locating and deleting old backups (rotation)

## Sample Log Output
See `sample_backup.log` for example log entries.

