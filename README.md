# Real Estate Django Web App

A Django web application for browsing real estate listings, managing realtors, and submitting contact inquiries. Includes a robust email fallback so inquiries are never lost.

## Features
- Listings with search and filters
- Realtor management via Django admin
- User accounts and dashboard of inquiries
- Contact inquiries with email sending and admin fallback
- Static assets and basic Bootstrap UI

## Email Inquiry & Admin Fallback
- Primary: sends inquiry to the listing's realtor email.
- Fallback: if realtor email is missing/invalid, or sending fails, the inquiry is sent to `ADMIN_EMAIL` (defaults to `DEFAULT_FROM_EMAIL`).
- `reply_to`: set to the client's email so replies go to the inquirer.

## Quick Start
- Requirements: Python 3.10+, pip, virtualenv
- Setup:
  - `python -m venv .venv && .\.venv\Scripts\activate`
  - `pip install -r requirements.txt`
  - `python manage.py migrate`
  - `python manage.py runserver`
- Visit: `http://127.0.0.1:8000/`

## Configuration
Set environment variables as needed (production SMTP vs. development console backend):
- `DEFAULT_FROM_EMAIL` – default sender address
- `ADMIN_EMAIL` – admin recipient for fallback (optional; defaults to `DEFAULT_FROM_EMAIL`)
- `EMAIL_HOST`, `EMAIL_PORT`, `EMAIL_HOST_USER`, `EMAIL_HOST_PASSWORD`, `EMAIL_USE_TLS` – SMTP settings

## Development Notes
- Admin: `http://127.0.0.1:8000/admin/`
- User dashboard shows inquiry details, including the message body.
- Screenshots: see `screenshots/` folder.

## Deployment
- Configure SMTP env vars and `ALLOWED_HOSTS`.
- Run `python manage.py collectstatic`.
- Use a WSGI server (e.g., gunicorn) behind a reverse proxy.

## License
MIT License. See `LICENSE`.
