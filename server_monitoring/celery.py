import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'server_monitoring.settings')

app = Celery('server_monitoring')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'fetch-server-data-every-15-minutes': {
        'task': 'monitoring.tasks.fetch_server_data',
        'schedule': crontab(minute='*/1'),
    },
    'monitor-resources-every-15-minutes': {
        'task': 'monitoring.tasks.monitor_resources',
        'schedule': crontab(minute='*/1'),
    },
}