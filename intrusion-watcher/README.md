# SSH Intrusion / Failed-Login Watcher

Parses auth.log for failed SSH login attempts, counts attempts per IP, and flags IPs exceeding a suspicious threshold (brute-force detection).

## Features
- Extracts failed SSH login attempts from auth.log
- Counts failed attempts per IP address
- Flags IPs with 10+ failed attempts as suspicious
- Simulates basic brute-force / intrusion detection

## Usage
```bash
chmod +x intrusion_watcher.sh
./intrusion_watcher.sh <path-to-auth.log>
```

## Tools Used
- `grep` — pattern matching for failed login lines
- `awk` — field extraction and threshold filtering
- `sort` / `uniq -c` — frequency counting per IP

## Sample Output
See `sample_auth.log` for example failed login data used to generate this report.
