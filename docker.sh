#!/bin/bash

# domain-checker Docker Helper Script
# Makes common Docker commands easier

set -e

COMPOSE_FILE="docker-compose.yml"
DEV_MODE=false

# Check if development mode is requested
if [[ "$1" == "dev" ]]; then
    COMPOSE_FILE="docker-compose.dev.yml"
    DEV_MODE=true
    shift  # Remove 'dev' from arguments
fi

COMMAND="${1:-help}"

case $COMMAND in
    help)
        echo "domain-checker Docker Helper"
        echo ""
        echo "Usage: ./docker.sh [dev] <command> [options]"
        echo ""
        echo "Development Mode:"
        echo "  ./docker.sh dev up         - Start development containers"
        echo "  ./docker.sh dev down       - Stop development containers"
        echo "  ./docker.sh dev logs       - View development logs"
        echo ""
        echo "Production Mode:"
        echo "  ./docker.sh up             - Start production containers"
        echo "  ./docker.sh down           - Stop production containers"
        echo "  ./docker.sh logs           - View production logs"
        echo "  ./docker.sh build          - Build production image"
        echo ""
        echo "Common Commands:"
        echo "  ./docker.sh [dev] shell    - Access Django shell"
        echo "  ./docker.sh [dev] dbshell  - Access PostgreSQL shell"
        echo "  ./docker.sh [dev] migrate  - Run migrations"
        echo "  ./docker.sh [dev] user     - Create superuser"
        echo "  ./docker.sh [dev] static   - Collect static files"
        echo "  ./docker.sh [dev] clean    - Remove containers and volumes"
        echo "  ./docker.sh [dev] rebuild  - Rebuild images"
        echo "  ./docker.sh [dev] status   - Show container status"
        echo ""
        ;;

    up)
        echo "🚀 Starting domain-checker..."
        docker-compose -f $COMPOSE_FILE up -d
        echo "✅ domain-checker is running"
        if [ "$DEV_MODE" = false ]; then
            echo "🌐 Access at: http://localhost"
        else
            echo "🌐 Access at: http://localhost:8000"
        fi
        ;;

    down)
        echo "🚫 Stopping domain-checker..."
        docker-compose -f $COMPOSE_FILE down
        echo "✅ domain-checker stopped"
        ;;

    logs)
        docker-compose -f $COMPOSE_FILE logs -f web
        ;;

    shell)
        echo "📝 Opening Django Shell..."
        docker-compose -f $COMPOSE_FILE exec web python manage.py shell
        ;;

    dbshell)
        echo "🗄️  Opening PostgreSQL Shell..."
        docker-compose -f $COMPOSE_FILE exec db psql -U admin -d domain_checker
        ;;

    migrate)
        echo "🔄 Running migrations..."
        docker-compose -f $COMPOSE_FILE exec web python manage.py migrate
        echo "✅ Migrations complete"
        ;;

    user)
        echo "👤 Creating superuser..."
        docker-compose -f $COMPOSE_FILE exec web python manage.py createsuperuser
        ;;

    static)
        echo "📦 Collecting static files..."
        docker-compose -f $COMPOSE_FILE exec web python manage.py collectstatic --noinput
        echo "✅ Static files collected"
        ;;

    clean)
        echo "🧹 Cleaning up..."
        docker-compose -f $COMPOSE_FILE down -v
        echo "✅ Cleanup complete"
        ;;

    rebuild)
        echo "🔨 Rebuilding images..."
        docker-compose -f $COMPOSE_FILE up -d --build
        echo "✅ Rebuild complete"
        ;;

    status)
        echo "📊 Container Status:"
        docker-compose -f $COMPOSE_FILE ps
        ;;

    bash)
        echo "🐚 Opening bash shell..."
        docker-compose -f $COMPOSE_FILE exec web bash
        ;;

    *)
        echo "Unknown command: $COMMAND"
        echo "Run './docker.sh help' for usage information"
        exit 1
        ;;
esac
