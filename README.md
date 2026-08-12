# DevOps Projects

A collection of shell scripting and Linux automation projects focused on system administration, log analysis, and security monitoring.

## Projects

### 1. [Automated Backup Script](./backup-automation)
Backs up directories with compression, timestamping, automatic rotation (deletes backups older than 7 days), and success/failure logging.

**Tools:** `tar`, `find`, `date`

### 2. [Nginx Log Analyzer](./log-analyzer)
Parses Nginx/Apache access logs to generate reports on traffic patterns — top IPs, status code breakdown, top requested paths, and suspicious scan detection (e.g. wp-login/admin probing).

**Tools:** `awk`, `grep`, `sort`, `uniq`

### 3. [SSH Intrusion Watcher](./intrusion-watcher)
Detects brute-force SSH attacks by parsing auth.log for failed login attempts and flagging IPs that exceed a suspicious threshold.

**Tools:** `grep`, `awk`, `sort`, `uniq`

## Skills Demonstrated
- Bash scripting and automation
- Log parsing and text processing (awk, grep, sed)
- Linux system administration
- Basic security monitoring / intrusion detection
- Git version control

## Author
Mit — [GitHub](https://github.com/mit-006)
