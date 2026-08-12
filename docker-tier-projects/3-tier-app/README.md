# 3-Tier Architecture — Task Tracker

A task tracker built with a proper 3-tier separation: Nginx (presentation/reverse proxy), Flask (application logic), and PostgreSQL (database), each in its own container.

## Architecture
Browser → Nginx (port 8080, public) → Flask (internal only) → PostgreSQL (internal only)

## Features
- Nginx acts as a reverse proxy — only Nginx is exposed to the host, Flask and the database are internal-only
- Add and complete tasks via a web form
- Database credentials passed via environment variables
- Data persists using a named Docker volume
- All 3 services communicate over a custom Docker network

## Usage
```bash
docker compose up -d --build
```

Visit `http://localhost:8080`

## Tools Used
- Nginx (reverse proxy)
- Flask (application layer)
- PostgreSQL (database layer)
- Docker Compose (multi-container orchestration)

## Why 3-Tier
This mirrors how real production systems are structured — each layer (presentation, application, data) can be scaled, secured, and maintained independently. 
The application server is never directly exposed to the internet;
all traffic is routed through Nginx first, which is a standard security practice
