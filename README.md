# domain-checker — Django Domain Checker

A modern Django-based domain checker application with user authentication, real-time DNS resolution, and RDAP domain registration lookup. **Fully containerized with Docker** for seamless deployment.

## Features

✨ **Core Features**
- Instant domain availability checks
- DNS resolution (A records, CNAME chains)
- RDAP registration data lookup
- Registrar information
- Registration & expiry dates
- Smart status detection

🔐 **Authentication**
- User registration and login
- Secure password hashing
- User profiles
- Session management
- Logout functionality

💾 **History & Storage**
- Save all domain checks
- View check history
- Detailed check information
- User-specific records

🎨 **User Interface**
- Dark theme with gradient accents
- Responsive mobile design
- Real-time results
- Beautiful animations
- Admin dashboard

🐳 **Docker Support**
- Production-ready Dockerfile
- Docker Compose with PostgreSQL & Nginx
- Development mode with hot-reload
- CI/CD workflow included
- Multi-environment support

Supports:
- Bare domains (`google.com`)
- Subdomains (`api.google.com`)
- Full URLs (`https://google.com`)

## Quick Start - Docker

### Prerequisites

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

### Launch (60 seconds)

```bash
# Navigate to project directory
cd Domain-checker

# Start services
docker-compose up -d

# Create admin account (optional)
docker-compose exec web python manage.py createsuperuser
```

**Access the app:**
- 🌐 Main app: http://localhost
- 🔧 Admin: http://localhost/admin
- 📚 API: http://localhost/checker

## Quick Start - Local Development

### Prerequisites

- Python 3.8+
- pip & virtualenv

### Installation

```bash
# 1. Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run migrations
python manage.py migrate

# 4. Create superuser (optional)
python manage.py createsuperuser

# 5. Start server
python manage.py runserver
```

Access at: http://127.0.0.1:8000

## Usage

### Sign Up
1. Visit the home page
2. Click "Get Started Free"
3. Create account with email and password

### Check Domains
1. Go to Checker
2. Enter domain name or URL
3. View instant results with IP addresses and registration data
4. Results saved to your check history

### View History
1. Click "History" in navigation
2. See all your previous checks
3. Click to view detailed information

## Docker Commands

### Production Setup (with Nginx + PostgreSQL)

```bash
# Start
docker-compose up -d

# Stop
docker-compose down

# View logs
docker-compose logs -f web

# Create superuser
docker-compose exec web python manage.py createsuperuser

# Database shell
docker-compose exec db psql -U domainpulse -d domainpulse
```

### Development Setup (faster, without Nginx)

```bash
# Start with hot-reload
docker-compose -f docker-compose.dev.yml up -d

# Stop
docker-compose -f docker-compose.dev.yml down

# View logs
docker-compose -f docker-compose.dev.yml logs -f web
```

### Using Helper Script

```bash
# Make script executable
chmod +x docker.sh

# Show all available commands
./docker.sh help

# Start production
./docker.sh up

# Start development
./docker.sh dev up

# View logs
./docker.sh logs

# Create superuser
./docker.sh user

# Access Django shell
./docker.sh shell

# Access database shell
./docker.sh dbshell
```

## Project Structure

```
Domain-checker/
├── domain_checker/           # Project config
│   ├── settings.py          # Django settings
│   ├── urls.py              # URL routing
│   └── wsgi.py              # WSGI app
├── users/                   # Authentication app
│   ├── models.py            # User models
│   ├── views.py             # Auth views
│   ├── forms.py             # Auth forms
│   └── urls.py              # Auth URLs
├── checker/                 # Domain checker app
│   ├── models.py            # Domain check model
│   ├── views.py             # Checker views
│   ├── utils.py             # Checking logic
│   └── urls.py              # Checker URLs
├── templates/               # HTML templates
│   ├── base.html            # Base layout
│   ├── home.html            # Home page
│   └── users/checker/       # Page templates
├── static/                  # CSS & static assets
│   └── styles.css           # Stylesheet
├── Dockerfile               # Docker image definition
├── docker-compose.yml       # Production compose config
├── docker-compose.dev.yml   # Development compose config
├── docker.sh                # Helper script
├── nginx.conf               # Nginx configuration
└── manage.py                # Django CLI
```

## Configuration

### Environment Variables

Create `.env` file from template:

```bash
cp .env.example .env
```

Edit `.env` with your settings:

```env
DEBUG=False
SECRET_KEY=your-very-secret-key-here
ALLOWED_HOSTS=localhost,127.0.0.1,yourdomain.com
DATABASE_URL=postgresql://user:password@db:5432/domain_checker
```

### Database

- **Development**: SQLite (local file)
- **Production**: PostgreSQL (in Docker)

### Static Files

```bash
# Collect static files locally
python manage.py collectstatic

# In Docker
docker-compose exec web python manage.py collectstatic --noinput
```

## API Endpoints

**Authentication**
- `POST /users/signup/` - Create new account
- `POST /users/login/` - Login user
- `GET /users/logout/` - Logout user

**Domain Checker**
- `GET /checker/` - Checker page (login required)
- `POST /checker/` - Check domain (login required)
- `GET /checker/history/` - View history (login required)
- `GET /checker/detail/<id>/` - View details (login required)

**Admin**
- `GET /admin/` - Admin dashboard

## Deployment

### Docker Hub / Private Registry
```bash
# Build image
docker build -t yourusername/domain-checker:latest .

# Push to registry
docker push yourusername/domain-checker:latest

# Deploy from image
docker pull yourusername/domain-checker:latest
docker-compose up -d
```

### Heroku
```bash
heroku create your-app-name
git push heroku main
heroku run python manage.py migrate
```

### AWS/GCP/Azure
Push Docker image to ECR/GCR/ACR, then deploy using cloud-specific instructions.

### Self-Hosted (Linux/VPS)
```bash
git clone <repo>
cd Domain-checker
cp .env.example .env
# Edit .env with your settings
docker-compose up -d
# Configure domain & SSL with reverse proxy (nginx/caddy)
```

## Documentation

- 📖 **Full Django Setup**: See [DJANGO_SETUP.md](DJANGO_SETUP.md)
- 🐳 **Docker Guide**: See [DOCKER_SETUP.md](DOCKER_SETUP.md)
- ⚡ **Docker Quick Start**: See [DOCKER_QUICKSTART.md](DOCKER_QUICKSTART.md)

## Troubleshooting

### Port 8000 Already in Use
```bash
# Development
python manage.py runserver 0.0.0.0:8001

# Docker
# Edit docker-compose.yml ports section
```

### Database Connection Error
```bash
# Reset database
docker-compose down -v
docker-compose up -d
```

### Static Files Not Loading
```bash
# Collect static files
python manage.py collectstatic --noinput

# In Docker
docker-compose exec web python manage.py collectstatic --noinput
docker-compose restart
```

### Permission Issues
```bash
# May need sudo
sudo docker-compose up -d --build
```

## Security

🔒 **Production Checklist**
- [ ] Change `SECRET_KEY` to random value
- [ ] Set `DEBUG=False`
- [ ] Configure `ALLOWED_HOSTS` to your domain(s)
- [ ] Setup SSL/HTTPS
- [ ] Change database password
- [ ] Use environment variables for secrets
- [ ] Set secure cookie flags
- [ ] Configure firewall/network ACLs
- [ ] Keep dependencies updated

## Performance

- Nginx caches static files (30 days)
- Database connection pooling
- Gunicorn with 4+ workers
- PostgreSQL for production
- CDN-ready architecture

## Support & Contributing

For issues and questions:

1. Check the documentation files
2. Review Django & Docker documentation
3. Open an Issue on GitHub
4. Submit pull requests are welcome!

## License

© 2024 domain-checker. All rights reserved.

## Resources

- [Django Documentation](https://docs.djangoproject.com/)
- [Docker Documentation](https://docs.docker.com/)
- [PostgreSQL Docs](https://www.postgresql.org/docs/)
- [Nginx Docs](https://nginx.org/en/docs/)
- [Gunicorn Docs](https://docs.gunicorn.org/)
