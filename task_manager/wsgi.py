import os
from django.core.wsgi import get_wsgi_application

# Set the default settings module for the 'DJANGO_SETTINGS_MODULE' environment variable
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'task_manager.settings')

# Get the WSGI application for use by servers or other tools
application = get_wsgi_application()
