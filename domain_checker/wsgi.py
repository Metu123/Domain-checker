"""
WSGI config for domain_checker project.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'domain_checker.settings')

application = get_wsgi_application()
