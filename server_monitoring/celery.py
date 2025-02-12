import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'server_monitoring.settings')

app = Celery('server_monitoring')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.update( #фикс с мультипроцессингом
    broker_url='redis://localhost:6379/0',
    result_backend=None,
    worker_pool='solo',
)