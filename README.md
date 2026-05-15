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


