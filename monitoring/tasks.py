import requests
from celery import shared_task
from datetime import timedelta
from .models import Incident, ServerResource
from celery import shared_task
from .models import Incident
from django.utils import timezone

@shared_task
def fetch_server_data():
    for server_id in range(1, 31):#30 серверов
        try:
            response = requests.get(f'http://127.0.0.1:8000/api/server/{server_id}/status/', timeout=10)
            if response.status_code != 200:
                print(f"Failed to fetch data for server {server_id}: {response.status_code}")
                continue

            data = response.json()
            ServerResource.objects.create(
                server_id=server_id,
                cpu=data.get('cpu', 0),
                mem=float(data.get('mem', '0').strip('%')),
                disk=float(data.get('disk', '0').strip('%')),
                uptime=data.get('uptime', '')
            )
        except Exception as e:
            print(f"Error fetching data for server {server_id}: {e}")

@shared_task
def monitor_resources():
    now = timezone.now()
    for server_id in range(1, 31):#30 серверов
        recent_data = ServerResource.objects.filter(server_id=server_id, timestamp__gte=now - timedelta(minutes=30))
        if recent_data.filter(cpu__gt=85).count() >= 2:
            Incident.objects.create(
                server_id=server_id,
                issue_type='CPU',
                description='CPU usage exceeded 85% for 30 minutes'
            )

        if recent_data.filter(mem__gt=90).count() >= 2:
            Incident.objects.create(
                server_id=server_id,
                issue_type='Mem',
                description='Memory usage exceeded 90% for 30 minutes'
            )
            
        disk_data = ServerResource.objects.filter(server_id=server_id, timestamp__gte=now - timedelta(hours=2))
        if disk_data.filter(disk__gt=95).count() >= 8:
            Incident.objects.create(
                server_id=server_id,
                issue_type='Disk',
                description='Disk usage exceeded 95% for 2 hours'
            )



"""
Нужно создать задачи которые будут отправлять каждые 15 минут запрашивать данные с серверов и сверять их с нормальными значениями

CPU > 85% в течение 30 минут
Mem > 90% в течение 30 минут
Disk > 95% в течение 2 часов
"""