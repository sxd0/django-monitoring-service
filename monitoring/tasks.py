import requests
from celery import shared_task
from django.utils.timezone import now
from datetime import timedelta
from .models import Incident
import psutil
from celery import shared_task
from .models import ServerMetric, Incident

@shared_task
def fetch_and_store_metrics():
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent

    metric = ServerMetric.objects.create(cpu_load=cpu, memory_usage=memory, disk_usage=disk)
    
    monitor_resources(metric.pk)

    return f"Metrics recorded: CPU={cpu}, Memory={memory}, Disk={disk}"

@shared_task
def monitor_resources(metric_id):
    metric = ServerMetric.objects.get(pk=metric_id)
    
    if metric.cpu_load > 85:
        Incident.objects.create(issue=f"CPU > 85%  : {metric.cpu_load}%")
    if metric.memory_usage > 90:
        Incident.objects.create(issue=f"Memory > 90%  : {metric.memory_usage}%")
    if metric.disk_usage > 95:
        Incident.objects.create(issue=f"Disk > 95%  : {metric.disk_usage}%")

    return "Monitoring complete"



"""
Нужно создать задачи которые будут отправлять каждые 15 минут запрашивать данные с серверов и сверять их с нормальными значениями

CPU > 85% в течение 30 минут
Mem > 90% в течение 30 минут
Disk > 95% в течение 2 часов
"""