from django.db import models

class ServerMetric(models.Model): #хранит в себе собранные метрики
    timestamp = models.DateTimeField(auto_now_add=True)
    cpu_load = models.FloatField()
    memory_usage = models.FloatField()
    disk_usage = models.FloatField()

    def __str__(self):
        return f"Metrics at {self.timestamp}"

class Incident(models.Model): #тут инциденты
    timestamp = models.DateTimeField(auto_now_add=True)
    issue = models.CharField(max_length=255)

    def __str__(self):
        return f"Incident at {self.timestamp}: {self.issue}"



"""
Нужно создать три модели:
1) список серверов
2) данные которые будут сохраняться с этих серверов
3) таблица в которой будут храниться инциденты после проверки
"""