#!/bin/bash
LOG_FILE=$1
THRESHOLD=10

if [ -z "$LOG_FILE" ]; then
    echo "Usage: ./intrusion_watcher.sh <auth_log_file>"
    exit 1
fi

echo "===== INTRUSION DETECTION REPORT ====="
echo "Log file: $LOG_FILE"
echo "Threshold: $THRESHOLD+ failed attempts = suspicious"
echo ""

echo "--- Failed login attempts by IP ---"
grep "Failed password" "$LOG_FILE" | awk '{print $NF, $0}' | awk '{for(i=1;i<=NF;i++) if($i=="from") print $(i+1)}' | sort | uniq -c | sort -nr

echo ""
echo "--- SUSPICIOUS IPs (>= $THRESHOLD attempts) ---"
grep "Failed password" "$LOG_FILE" | awk '{print $NF, $0}' | awk '{for(i=1;i<=NF;i++) if($i=="from") print $(i+1)}' | sort | uniq -c | sort -nr | awk -v t="$THRESHOLD" '$1 >= t {print $2, "-", $1, "failed attempts"}'
