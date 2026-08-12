#!/bin/bash
LOG_FILE=$1
REPORT_FILE="log_report_$(date +%Y-%m-%d_%H-%M-%S).txt"

if [ -z "$LOG_FILE" ]; then
    echo "Usage: ./log_analyzer.sh <access_log_file>"
    exit 1
fi

{
echo "===== LOG ANALYSIS REPORT ====="
echo "File: $LOG_FILE"
echo "Generated: $(date)"
echo ""

echo "--- Top 5 IPs by request count ---"
awk 'NF{print $1}' "$LOG_FILE" | sort | uniq -c | sort -nr | head -5

echo ""
echo "--- Status Code Breakdown ---"
awk 'NF{print $9}' "$LOG_FILE" | sort | uniq -c | sort -nr

echo ""
echo "--- Top 10 Requested Paths ---"
awk 'NF{print $7}' "$LOG_FILE" | sort | uniq -c | sort -nr | head -10

echo ""
echo "--- Total 404 errors ---"
grep -c '" 404 ' "$LOG_FILE"

echo ""
echo "--- Total 500 errors ---"
grep -c '" 500 ' "$LOG_FILE"

echo ""
echo "--- Suspicious: wp-login / admin scan attempts ---"
grep -E 'wp-login|/admin' "$LOG_FILE"

echo ""
echo "--- All 404 requests (detail) ---"
grep '" 404 ' "$LOG_FILE"

echo ""
echo "===== END OF REPORT ====="
} > "$REPORT_FILE"

echo "Report saved to: $REPORT_FILE"
