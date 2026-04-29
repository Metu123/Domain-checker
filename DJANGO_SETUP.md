# domain-checker — Django Domain Checker with Authentication

A modern Django-based domain checker application with user authentication (login, signup, logout), real-time DNS resolution, and RDAP domain registration lookup.

## Features

✨ **Authentication**
- User registration (signup)
- Secure login
- Logout functionality
- User profiles

🔍 **Domain Checking**
- DNS resolution (A records)
- CNAME chains
- IP address lookup
- RDAP registration data
- Registrar information
- Registration & expiry dates

💾 **History Management**
- Save all domain checks
- View check history
- Detailed check information

🎨 **Modern UI**
- Dark theme with gradient accents
- Responsive design
- Real-time status updates
- Beautiful animations

## Prerequisites

- Python 3.8+
- pip (Python package manager)
- Virtual environment (recommended)

## Installation

### 1. Clone/Download the Project

```bash
cd /workspaces/Domain-checker
```

### 2. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply Migrations

```bash
python manage.py migrate
```

### 5. Create Superuser (Optional - for Admin Panel)

```bash
python manage.py createsuperuser
```

Follow the prompts to create an admin account.

### 6. Run Development Server

```bash
python manage.py runserver
```

The application will be available at `http://127.0.0.1:8000/`

## Usage

### First Time Users

1. Go to http://127.0.0.1:8000/
2. Click "Get Started Free" or "Sign Up"
3. Create your account
4. Start checking domains!

### Logging In

1. Visit http://127.0.0.1:8000/users/login/
2. Enter username/email and password
3. Click Login

### Checking Domains

1. Go to http://127.0.0.1:8000/checker/
2. Enter a domain (examples: `google.com`, `https://example.com`, `api.github.com`)
3. View instant results showing:
   - Domain status (active/registered/not found)
   - IP addresses
   - Registrar information
   - Registration dates

### Viewing History

1. Click "History" in navigation
2. See all your previous domain checks
3. Click "View Details" for full information

## Project Structure

```
Domain-checker/
├── domain_checker/          # Project configuration
│   ├── settings.py         # Django settings
│   ├── urls.py             # URL configuration
│   └── wsgi.py             # WSGI application
├── users/                  # Authentication app
│   ├── models.py           # User profiles
│   ├── views.py            # Auth views (login, signup, logout)
│   ├── forms.py            # Authentication forms
│   └── urls.py             # Auth URLs
├── checker/                # Domain checker app
│   ├── models.py           # DomainCheck model
│   ├── views.py            # Checker views
│   ├── utils.py            # Domain checking logic
│   ├── forms.py            # Checker forms
│   └── urls.py             # Checker URLs
├── templates/              # HTML templates
│   ├── base.html           # Base template
│   ├── home.html           # Home page
│   └── users/              # Auth templates
│   └── checker/            # Checker templates
├── static/                 # CSS and static files
│   └── styles.css          # Stylesheet
├── manage.py               # Django management script
└── requirements.txt        # Python dependencies
```

## API Endpoints

**Authentication:**
- `POST /users/signup/` - Create new account
- `POST /users/login/` - Login user
- `GET /users/logout/` - Logout user

**Domain Checker:**
- `GET /checker/` - Checker page (login required)
- `POST /checker/` - Check domain (login required)
- `GET /checker/history/` - View check history (login required)
- `GET /checker/detail/<id>/` - View check details (login required)

**Admin:**
- `GET /admin/` - Admin panel (create superuser first)

## Configuration

### Settings (domain_checker/settings.py)

Key settings you might want to customize:

```python
DEBUG = True  # Set to False in production
ALLOWED_HOSTS = ['*']  # Configure for your domain
SECRET_KEY = 'your-secret-key'  # Change in production
```

### Database

Default: SQLite3 (db.sqlite3) - suitable for development

For production, consider:
- PostgreSQL
- MySQL
- MariaDB

## Troubleshooting

### Port 8000 already in use

```bash
python manage.py runserver 8001
```

### Database errors

```bash
rm db.sqlite3
python manage.py migrate
```

### Module not found errors

```bash
pip install -r requirements.txt
```

### Static files not loading

```bash
python manage.py collectstatic --noinput
```

## Security Notes

⚠️ **Development Only**
- `DEBUG = True` - Never use in production
- `SECRET_KEY` - Change this before deploying
- `ALLOWED_HOSTS` - Set to your domain(s)

## Deployment

For production deployment, consider:

1. Set `DEBUG = False`
2. Use a production database (PostgreSQL, MySQL)
3. Use a production web server (Gunicorn, uWSGI)
4. Set up proper `SECRET_KEY` and `ALLOWED_HOSTS`
5. Enable HTTPS/SSL
6. Set secure cookie settings

Example with Gunicorn:
```bash
pip install gunicorn
gunicorn domain_checker.wsgi:application
```

## License

© 2024 domain-checker. All rights reserved.

## Support

For issues or questions, please check:
1. Django documentation: https://docs.djangoproject.com/
2. Python requests library: https://requests.readthedocs.io/
