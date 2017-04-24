# GeoDjango Query

Use a combination of Django, Django Rest Framework, and Postgres with PostGis and Geodjango to return a list of points within a provided radius.

## Installation

You'll need a few things before we get started.

```bash
pip install -r requirements.txt
```

Depending on your operating system, you'll need to install gdal (libgdal-dev) in different ways. On a Mac, it's

```bash
brew install gdal
```

## Setup

Change usernames, passwords, ports in geodata/settings.py

From a privileged POSTGRES shell, run:

```sql
CREATE USER yourusernamehere PASSWORD 'yourpasswordhere';
CREATE DATABASE yourdatabasenamehere OWNER yourusernamehere;
```

From a POSTGRES shell using your new database, run:

```sql
CREATE EXTENSION postgis;
```

```bash
python manage.py migrate
```

```bash
python manage.py runserver
```

Navigate to 127.0.0.1:8000
