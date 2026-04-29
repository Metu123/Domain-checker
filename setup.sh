#!/bin/bash

# domain-checker Django Setup Script
# This script sets up the Django development environment

echo "🚀 Setting up domain-checker Django Application..."

# Check Python
echo "✓ Checking Python installation..."
python3 --version

# Create virtual environment
echo "✓ Creating virtual environment..."
python3 -m venv venv

# Activate virtual environment
echo "✓ Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "✓ Installing dependencies..."
pip install -r requirements.txt

# Run migrations
echo "✓ Running database migrations..."
python manage.py migrate

# Create superuser (optional)
read -p "Would you like to create a superuser now? (y/n) " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    python manage.py createsuperuser
fi

echo ""
echo "✅ Setup complete!"
echo ""
echo "🎉 To start the development server, run:"
echo "   source venv/bin/activate"
echo "   python manage.py runserver"
echo ""
echo "📖 For more information, see DJANGO_SETUP.md"
