# Docker Setup - domain-checker

This project is fully containerized with Docker for easy deployment.

## Docker Compose Services

The `docker-compose.yml` includes:

- **PostgreSQL Database** - Persistent data storage
- **Django Web Application** - Built with Gunicorn
- **Nginx** - Reverse proxy and static file server

## Prerequisites

- Docker - [Install Docker](https://docs.docker.com/get-docker/)
- Docker Compose - [Install Docker Compose](https://docs.docker.com/compose/install/)

## Quick Start

### 1. Clone/Navigate to Project

```bash
cd /workspaces/Domain-checker
```

### 2. Configure Environment (Optional)

Copy `.env.example` to `.env` and customize if needed:

```bash
cp .env.example .env
```

### 3. Build and Run

```bash
docker-compose up -d
```

This will:
- Build the Django image
- Create and start PostgreSQL
- Create and start Nginx
- Run database migrations
- Collect static files

### 4. Access the Application

- **Main App**: http://localhost
- **Django Admin**: http://localhost/admin/
- **Direct Django**: http://localhost:8000

## Common Commands

### View logs
```bash
docker-compose logs -f web
```

### Create superuser
```bash
docker-compose exec web python manage.py createsuperuser
```

### Run migrations
```bash
docker-compose exec web python manage.py migrate
```

### Stop containers
```bash
docker-compose down
```

### Stop and remove all data
```bash
docker-compose down -v
```

### Rebuild image
```bash
docker-compose up -d --build
```

### Shell access to Django container
```bash
docker-compose exec web bash
```

### Shell access to Database
```bash
docker-compose exec db psql -U admin -d domain_checker
```

## Production Deployment

### Important: Change These Values

Before deploying to production, edit your `.env` file:

```env
DEBUG=False
SECRET_KEY=your-very-secure-random-key-here
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
SECURE_SSL_REDIRECT=True
SESSION_COOKIE_SECURE=True
CSRF_COOKIE_SECURE=True
```

### Generate Secure Secret Key

```bash
docker-compose exec web python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

### Use with Docker Swarm or Kubernetes

The setup is compatible with:
- Docker Swarm
- Kubernetes (with minor modifications)
- AWS ECS
- Google Cloud Run
- Azure Container Instances

### SSL/HTTPS Setup

To enable HTTPS:

1. Add SSL certificates to the project
2. Update nginx.conf with SSL configuration
3. Update docker-compose.yml port mapping
4. Set `SECURE_SSL_REDIRECT=True` in .env

Example SSL in nginx.conf:
```nginx
server {
    listen 80;
    listen 443 ssl http2;
    
    ssl_certificate /app/certs/cert.pem;
    ssl_certificate_key /app/certs/key.pem;
    
    # ... rest of config
}
```

## Database

### PostgreSQL Credentials (from docker-compose.yml)

- **User**: admin
- **Password**: secure_password
- **Database**: domain_checker
- **Host**: db (internal) or localhost:5432 (external)

### Backup Database

```bash
docker-compose exec db pg_dump -U admin domain_checker > backup.sql
```

### Restore Database

```bash
docker-compose exec -T db psql -U admin domain_checker < backup.sql
```

## Static Files

- Served by Nginx at `/static/`
- Collected during container startup
- Located in `static_volume` Docker volume

## Troubleshooting

### Port already in use

Change the port in docker-compose.yml:

```yaml
ports:
  - "8080:8000"  # Changed from 8000:8000
```

Then access at http://localhost:8080

### Database connection error

Ensure PostgreSQL is healthy:

```bash
docker-compose ps
```

Check logs:
```bash
docker-compose logs db
```

### Static files not loading

Rebuild and restart:

```bash
docker-compose down
docker-compose up -d --build
```

### Permission denied errors

May need to rebuild as root:
```bash
sudo docker-compose up -d --build
```

## Performance Tuning

### Increase Worker Processes

Edit Dockerfile:
```dockerfile
CMD ["gunicorn", "domain_checker.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "8"]
```

### Database Connection Pooling

Add to docker-compose.yml web service environment:
```yaml
- DATABASE_POOL_SIZE=20
- DATABASE_MAX_OVERFLOW=10
```

## Security Best Practices

✅ Change the database password in production  
✅ Use a strong SECRET_KEY  
✅ Enable SSL/HTTPS  
✅ Configure ALLOWED_HOSTS correctly  
✅ Use environment variables for secrets  
✅ Regularly update base images  
✅ Use network policies/firewalls  
✅ Set up log aggregation  
✅ Monitor container resources  

## Development vs Production

### Development (Current Setup)
- DEBUG=True
- SQLite or PostgreSQL
- Single worker
- No SSL

### Production Changes Needed
- DEBUG=False
- PostgreSQL required
- Multiple workers
- SSL/HTTPS enabled
- Strong SECRET_KEY
- Environment-specific settings

## Additional Resources

- [Docker Documentation](https://docs.docker.com/)
- [Docker Compose Reference](https://docs.docker.com/compose/compose-file/)
- [Django Deployment](https://docs.djangoproject.com/en/stable/howto/deployment/)
- [Gunicorn Configuration](https://docs.gunicorn.org/)
- [Nginx Documentation](https://nginx.org/en/docs/)
