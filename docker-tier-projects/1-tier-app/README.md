# 1-Tier Architecture — Task Tracker

A simple task tracker web app where the frontend (HTML), backend logic (Flask), and database (SQLite) all run inside a single container.

## Architecture
[ Single Container ]
Frontend (HTML) + Backend (Flask) + Database (SQLite)

## Features
- Add tasks via a web form
- Mark tasks as done
- Data persists in a SQLite file inside the container

## Usage

### Build
```bash
docker build -t task-tracker-1tier .
```

### Run
```bash
docker run -d -p 5000:5000 --name task-app task-tracker-1tier
```

Visit `http://localhost:5000`

## Tools Used
- Flask (Python web framework)
- SQLite (file-based database)
- Docker

## Note
This is a monolithic (1-tier) setup — everything runs in one container. This is not how production apps are typically deployed, but it's useful for understanding the baseline before moving to 2-tier and 3-tier architectures where components are separated into different containers.
