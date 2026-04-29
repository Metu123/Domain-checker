# 🐳 Docker Setup Complete!

Your domain-checker Django application is now fully containerized! Here's what was added:

## 📦 New Docker Files

```
├── Dockerfile                   # Django application image
├── docker-compose.yml           # Production setup (with Nginx + PostgreSQL)
├── docker-compose.dev.yml       # Development setup (without Nginx)
├── docker.sh                    # Helper script for common commands
├── nginx.conf                   # Nginx reverse proxy configuration
├── .dockerignore               # Files to exclude from Docker image
├── .env.example                # Environment variables template
├── DOCKER_SETUP.md             # Docker documentation
└── .github/workflows/
    └── docker-build.yml         # CI/CD workflow
```

## 🚀 Quick Start

### Option 1: Production (with Nginx)

```bash
# Build and start all services
docker-compose up -d

# Access the application
open http://localhost
```

### Option 2: Development (without Nginx, hot-reload)

```bash
# Use development compose file
docker-compose -f docker-compose.dev.yml up -d

# Access the application
open http://localhost:8000
```

### Option 3: Using Helper Script

```bash
# Make script executable
chmod +x docker.sh

# Development mode
./docker.sh dev up

# Production mode
./docker.sh up

# View all commands
./docker.sh help
```

## 📋 Services

### Production Stack (docker-compose.yml)
- **PostgreSQL** - Database on port 5432
- **Django** - Web app on port 8000 (internal)
- **Nginx** - Reverse proxy on port 80

### Development Stack (docker-compose.dev.yml)
- **PostgreSQL** - Database on port 5432
- **Django** - Web app on port 8000 (direct access)

## 🎯 Common Tasks

### Create Admin User
```bash
# Production
docker-compose exec web python manage.py createsuperuser

# Development
docker-compose -f docker-compose.dev.yml exec web python manage.py createsuperuser

# Using helper script
./docker.sh user          # Production
./docker.sh dev user      # Development
```

### View Logs
```bash
# Production
docker-compose logs -f web

# Development
docker-compose -f docker-compose.dev.yml logs -f web

# Using helper script
./docker.sh logs          # Production
./docker.sh dev logs      # Development
```

### Database Shell
```bash
# Production
docker-compose exec db psql -U admin -d domain_checker

# Development
docker-compose -f docker-compose.dev.yml exec db psql -U admin -d domain_checker

# Using helper script
./docker.sh dbshell       # Production
./docker.sh dev dbshell   # Development
```

### Stop Services
```bash
# Production
docker-compose down

# Development
docker-compose -f docker-compose.dev.yml down

# Using helper script
./docker.sh down          # Production
./docker.sh dev down      # Development
```

## 🔐 Configuration

Copy the environment template and customize:

```bash
cp .env.example .env
```

Edit `.env` with your settings:

```env
DEBUG=False
SECRET_KEY=your-secure-key-here
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=postgresql://admin:password@db:5432/domain_checker
```

## 🐛 Troubleshooting

### Port Already in Use

Edit `docker-compose.yml` to use different ports:

```yaml
ports:
  - "8080:80"    # Changed from 80:80
```

### Database Connection Error

```bash
# Check database status
docker-compose ps

# View database logs
docker-compose logs db

# Rebuild and restart
docker-compose down -v
docker-compose up -d
```

### Static Files Not Loading

```bash
# Collect static files
docker-compose exec web python manage.py collectstatic --noinput

# Or rebuild
docker-compose up -d --build
```

## 📚 Documentation

- **Full Docker Guide**: See `DOCKER_SETUP.md`
- **Django Setup**: See `DJANGO_SETUP.md`
- **Docker API Reference**: See `docker.sh help`

## 🆘 Helper Script Reference

```bash
./docker.sh help          # Show all commands
./docker.sh up            # Start production
./docker.sh dev up        # Start development
./docker.sh down          # Stop services
./docker.sh dev down      # Stop development
./docker.sh logs          # View logs
./docker.sh dev logs      # View dev logs
./docker.sh migrate       # Run migrations
./docker.sh user          # Create superuser
./docker.sh shell         # Django shell
./docker.sh dbshell       # PostgreSQL shell
./docker.sh bash          # Bash in container
./docker.sh clean         # Remove everything
./docker.sh rebuild       # Rebuild images
./docker.sh status        # Show container status
```

## 🎉 You're Ready!

Your application is now containerized and ready to deploy:

1. **Development**: `docker-compose -f docker-compose.dev.yml up`
2. **Production**: `docker-compose up`
3. **Deployment**: Push to your Docker Hub, AWS ECR, etc.

For detailed information, see `DOCKER_SETUP.md`.
