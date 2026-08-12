# DevOps Projects

A collection of shell scripting, Docker, and Linux automation projects focused on system administration, containerization, and security monitoring.

## Shell Scripting Projects

### 1. [Automated Backup Script](./backup-automation)
Backs up directories with compression, timestamping, automatic rotation (deletes backups older than 7 days), and success/failure logging.

**Tools:** `tar`, `find`, `date`

### 2. [Nginx Log Analyzer](./log-analyzer)
Parses Nginx/Apache access logs to generate reports on traffic patterns — top IPs, status code breakdown, top requested paths, and suspicious scan detection.

**Tools:** `awk`, `grep`, `sort`, `uniq`

### 3. [SSH Intrusion Watcher](./intrusion-watcher)
Detects brute-force SSH attacks by parsing auth.log for failed login attempts and flagging IPs that exceed a suspicious threshold.

**Tools:** `grep`, `awk`, `sort`, `uniq`

## Docker Architecture Projects

A progression of the same task tracker app built across three architectures, demonstrating containerization, networking, and separation of concerns.

### 4. [1-Tier Architecture](./docker-tier-projects/1-tier-app)
Frontend, backend, and database (SQLite) all running in a single container.

### 5. [2-Tier Architecture](./docker-tier-projects/2-tier-app)
App (Flask) and database (PostgreSQL) split into separate containers, communicating over a custom Docker network.

### 6. [3-Tier Architecture](./docker-tier-projects/3-tier-app)
Nginx (reverse proxy) + Flask (application) + PostgreSQL (database), each in its own container. Only Nginx is exposed to the host — the app and database are internal-only.

**Tools:** Docker, Docker Compose, Flask, PostgreSQL, Nginx

## Skills Demonstrated
- Bash scripting and automation
- Log parsing and text processing (awk, grep, sed)
- Linux system administration
- Basic security monitoring / intrusion detection
- Docker containerization and multi-container orchestration
- Container networking (custom bridge networks, service discovery)
- Reverse proxy configuration (Nginx)
- Environment-based configuration and data persistence (volumes)
- Git version control

## Author
Mit — [GitHub](https://github.com/mit-006)
