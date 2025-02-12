import requests
from celery import shared_task
from .models import Machine, ResourceUsage
from django.utils.timezone import now
from datetime import timedelta
from .models import ResourceUsage, Incident


@shared_task
def fetch_and_store_metrics():
    machines = Machine.objects.all()
    for machine in machines:
        response = requests.get(f'http://{machine.ip_address}/metrics')
        if response.status_code == 200:
            data = response.json()
            ResourceUsage.objects.create(
                machine=machine,
                cpu=data['cpu'],
                mem=float(data['mem'].replace('%', '')),
                disk=float(data['disk'].replace('%', '')),
                uptime=data['uptime']
            )

@shared_task
def monitor_resources():
    threshold = {'cpu': 85, 'mem': 90, 'disk': 95}
    time_limits = {'cpu': 30, 'mem': 30, 'disk': 120}

    for resource, limit in threshold.items():
        recent_data = ResourceUsage.objects.filter(
            timestamp__gte=now() - timedelta(minutes=time_limits[resource])
        )
        if recent_data.exists():
            avg_value = sum(getattr(d, resource) for d in recent_data) / len(recent_data)
            if avg_value > limit:
                Incident.objects.create(machine=recent_data[0].machine, resource=resource, value=avg_value)


"""
Нужно создать задачи которые будут отправлять каждые 15 минут запрашивать данные с серверов и сверять их с нормальными значениями

CPU > 85% в течение 30 минут
Mem > 90% в течение 30 минут
Disk > 95% в течение 2 часов
"""