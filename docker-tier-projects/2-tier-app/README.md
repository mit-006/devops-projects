# 2-Tier Architecture — Task Tracker

A task tracker where the application (frontend + backend) and database run in separate containers, connected over a custom Docker network.

## Architecture
[ App Container: Flask ] <--network--> [ DB Container: PostgreSQL ]

## Features
- Add and complete tasks via a web form
- Database runs in a separate container from the app
- Database credentials passed via environment variables (not hardcoded)
- Data persists using a named Docker volume
- App retries connecting to the database on startup (handles startup timing)

## Usage
```bash
docker compose up -d --build
```

Visit `http://localhost:5000`

## Tools Used
- Flask (Python web framework)
- PostgreSQL (relational database)
- Docker Compose (multi-container orchestration)
- Docker networks and volumes

## Why 2-Tier
Separating the database into its own container means the database can be scaled, backed up, or restarted independently of the application. This is a step up from a 1-tier monolithic setup and closer to how real applications are deployed.
