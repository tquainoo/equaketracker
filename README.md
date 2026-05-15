# Earthquake Analytics Platform

## Features

- Flask analytics platform
- Multiple linked database tables
- Earthquake dashboard
- Search functionality
- Regional analytics
- Chart.js visualizations
- Bootstrap responsive UI
- Error handling
- Advanced testing
- Render deployment support

## Database Tables

1. Country
2. Region
3. Earthquake

## Installation

```bash
python -m venv venv
pip install -r requirements.txt
python seed.py
python run.py
```

## Tests

```bash
pytest --cov=app
```

## Deployment

Start Command:

```bash
gunicorn run:app
```

## Git Log

```bash
git log --pretty=format:'%h : %s' --graph > git-log.txt
```