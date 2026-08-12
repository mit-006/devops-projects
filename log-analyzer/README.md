# Nginx Log Analyzer

A bash script that parses Nginx/Apache access logs and generates a summary report — top IPs, status code breakdown, top requested paths, and suspicious activity detection.

## Features
- Top 5 IPs by request count
- HTTP status code breakdown (200, 404, 500, etc.)
- Top 10 requested paths
- 404 and 500 error counts
- Detects suspicious scan attempts (e.g. wp-login, /admin probes)
- Saves timestamped report to a file

## Usage
```bash
chmod +x log_analyzer.sh
./log_analyzer.sh <path-to-access-log>
```

## Tools Used
- `awk` — field-based parsing (IP, status code, path extraction)
- `grep` — pattern matching for errors and suspicious requests
- `sort` / `uniq -c` — frequency counting

## Sample Output
See `sample_access.log` for the input log used to generate reports.
