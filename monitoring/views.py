from django.http import JsonResponse
import random

def mock_server_status(request, server_id): #заглушка
    cpu = random.randint(10, 100)
    mem = f"{random.randint(10, 100)}%"
    disk = f"{random.randint(10, 100)}%"
    uptime = "1d 2h 37m 6s"

    return JsonResponse({
        "cpu": cpu,
        "mem": mem,
        "disk": disk,
        "uptime": uptime
    })