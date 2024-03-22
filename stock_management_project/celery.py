from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Set Django settings for Celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'stock_management_project.settings')

# Create an instance of the Celery application
app = Celery('stock_management_project')

# Configure Celery using Django configuration
app.config_from_object('django.conf:settings', namespace='CELERY')

# Discover tasks in all registered Django modules
app.autodiscover_tasks()