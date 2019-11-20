import os
from celery import Celery
# from celery import task  

# celery = Celery('tasks', broker='amqp://guest@localhost//')
# os.environ[ 'DJANGO_SETTINGS_MODULE' ] = "proj.settings"
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')

# name of proj = 'app'
app = Celery('app')
app.config_from_object('django.conf:settings')
 
# Load task modules from all registered Django app configs.
app.autodiscover_tasks()