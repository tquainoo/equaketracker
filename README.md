# Earthquake Analytics Platform

A database-driven web application built with **Flask** that collects, stores, and analyzes earthquake data.  
The system provides an interactive analytics dashboard with search, filtering, pagination, and statistical insights.

---

# Project Overview

The Earthquake Analytics Platform is designed to:

- Store earthquake data in a relational database
- Provide analytical insights (magnitude, depth, region distribution)
- Enable fast search and filtering
- Display strongest and recent earthquakes
- Support scalable deployment using PostgreSQL (Render)

The system follows a **clean MVC architecture using Flask Blueprints**.

---

# System Design

## Architecture Style
- MVC (Model–View–Controller)
- Blueprint-based Flask structure

## Components

### 1. Models (Data Layer)
- Earthquake
- Region
- Country

Stored using SQLAlchemy ORM.

---

### 2. Views (Presentation Layer)
- dashboard.html
- earthquake_detail.html
- region_detail.html
- error pages (404, 500)

Built using **Jinja2 templating engine + Bootstrap UI**

---

### 3. Controllers (Logic Layer)
- routes.py handles:
  - Dashboard analytics
  - Search & filtering
  - Pagination
  - Detail views

---

### 4. Database
- SQLite (development)
- PostgreSQL (production on Render)

---

# Technology Stack

| Layer | Technology |
|------|------------|
| Backend | Flask (Python) |
| ORM | SQLAlchemy |
| Database | SQLite / PostgreSQL |
| Frontend | HTML, Bootstrap |
| Template Engine | Jinja2 |
| Deployment | Render |
| WSGI Server | Gunicorn |

---

# System Implementation
Installation Guide
1. Clone the Repository
git clone https://github.com/yourusername/earthquake-tracker.git
cd earthquake-tracker
2. Create a Virtual Environment
Windows
python -m venv venv
venv\Scripts\activate
Linux / macOS
python3 -m venv venv
source venv/bin/activate
3. Install Dependencies
pip install -r requirements.txt
Database Configuration
SQLite (Local Development)

The application uses SQLite by default for local testing.

Example configuration:

SQLALCHEMY_DATABASE_URI = 'sqlite:///earthquakes.db'
PostgreSQL (Production)

Set the environment variable:

DATABASE_URL=postgresql://username:password@host:port/dbname

Example Flask configuration:

import os

SQLALCHEMY_DATABASE_URI = os.getenv(
    "DATABASE_URL",
    "sqlite:///earthquakes.db"
)
Database Migration

Initialize migrations:

flask db init

Create migration:

flask db migrate -m "Initial migration"

Apply migration:

flask db upgrade
Loading Earthquake Data

Run the seed script:

python seed.py

This imports earthquake records from the dataset into the database.

Running the Application Locally

Start the Flask server:

python run.py

Open in browser:

http://127.0.0.1:5000
Deployment Guide (Render)
1. Push Project to GitHub
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/yourusername/earthquake-tracker.git
git push -u origin main
2. Create PostgreSQL Database on Render
Login to Render
Create a new PostgreSQL database
Copy the External Database URL
3. Create Web Service on Render
Select New Web Service
Connect GitHub repository
Choose Python environment
Build Command
pip install -r requirements.txt
Start Command
gunicorn run:app
4. Add Environment Variables

Add these variables in Render dashboard:

Variable	Value
DATABASE_URL	PostgreSQL External URL
SECRET_KEY	Your secret key
5. Deploy

Click Deploy Web Service.

Render automatically:

installs dependencies
builds the application
starts the Flask server
API Endpoints
Endpoint	Description
/	Dashboard
/earthquakes	Earthquake records
/api/earthquakes	JSON earthquake data
Pagination & Filtering

The application supports:

pagination
magnitude filtering
location filtering
date filtering

Example:

/earthquakes?page=2
Common Errors & Fixes
Error: SQLALCHEMY_DATABASE_URI must be set

Solution:

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")
Error: psycopg2 module missing

Install:

pip install psycopg2-binary
Error: Failed to push refs to GitHub

Run:

git pull origin main --rebase
git push origin main

