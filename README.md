# Real Estate Django Web App

A modern real estate listings website built with Django, Bootstrap, and vanilla JS. It includes user registration/login, listing management, inquiry handling with email notifications, and an admin panel.

## Features

- Browse and search property listings
- User registration, login, and dashboard
- Admin panel for managing listings and realtors
- Contact inquiry email with admin fallback
- Responsive UI with Bootstrap

## Tech Stack

- Python, Django
- Bootstrap 4, vanilla JS
- SQLite (default) or PostgreSQL

## Quick Start (Windows/macOS/Linux)

1. Clone the repo

```bash
git clone https://github.com/LancineDev/Real-Estate-Django-Web-App.git
cd Real-Estate-Django-Web-App
```

2. Create a virtual environment and install dependencies

```bash
python -m venv .venv
# Windows
.\.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

pip install -r requirements.txt
```

3. Apply migrations and create a superuser (optional)

```bash
python manage.py migrate
python manage.py createsuperuser
```

4. Run the development server

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/`.

## Configuration

All configuration is in `realestate/settings.py`.

- Email sending
  - Uses SMTP in production if configured; otherwise uses the console backend for development.
  - Fallback behavior: inquiries send to the realtor; if the realtor email is missing/invalid or sending fails, the email is automatically sent to `ADMIN_EMAIL`.
  - The inquirer’s email is set as `reply_to`.

- Environment variables (recommended)

```bash
# Fallback recipient for inquiries (if realtor email missing/fails)
ADMIN_EMAIL="admin@example.com"
# Default from address
DEFAULT_FROM_EMAIL="noreply@example.com"

# SMTP configuration (example for Gmail with App Password)
EMAIL_HOST="smtp.gmail.com"
EMAIL_PORT=587
EMAIL_HOST_USER="you@example.com"
EMAIL_HOST_PASSWORD="your_app_password"
EMAIL_USE_TLS=true
# Or, if you use SSL
# EMAIL_PORT=465
# EMAIL_USE_SSL=true
```

### Database

- Default: SQLite (no extra setup)
- PostgreSQL (optional): update `DATABASES` in `realestate/settings.py`.

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'real_estate',
        'USER': 'postgres',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

## Screenshots

- Home: `screenshots/s1.JPG`
- Listings: `screenshots/s3list.JPG`
- Registration: `screenshots/s4reg.JPG`
- Admin Panel: `screenshots/s5adm.JPG`, `screenshots/s6r.JPG`
- About: `screenshots/s2about.JPG`

## Deployment

See `Django_Deployment_to_Ubuntu_18.04.md` for a step‑by‑step guide.

## License

MIT — see `LICENSE`.

## Acknowledgments

Inspired by Brad Traversy’s Django course and based on the original project by TheCaffeineDev, updated and maintained here.
