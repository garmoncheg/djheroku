import os
from celery import Celery
from django.conf import settings


# Lets the celery command line program know where project settings are.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djheroku.settings')

# Creates the instance of the Celery app.
app = Celery('djheroku')

app.config_from_object('djheroku:settings', namespace='CELERY')

# Set up autodiscovery of tasks in the INSTALLED_APPS.
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

if __name__ == '__main__':
    app.start()