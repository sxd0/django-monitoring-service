import os
from celery import Celery
from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'server_monitoring.settings')

app = Celery('server_monitoring')

app.conf.beat_schedule = {
    'fetch-metrics-every-minute': {
        'task': 'monitoring.tasks.fetch_and_store_metrics',
        'schedule': crontab(minute='*/1'),
    },
}

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()


# app.conf.update( #фикс с мультипроцессингом
#     broker_url='redis://localhost:6379/0',
#     result_backend=None,
#     worker_pool='solo',
# )




