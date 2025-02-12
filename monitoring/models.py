from django.db import models



class ServerResource(models.Model): #хранение данных нагрузка
    server_id = models.IntegerField()
    cpu = models.FloatField()
    mem = models.FloatField()
    disk = models.FloatField()
    uptime = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Server {self.server_id} - {self.timestamp}"

class Incident(models.Model): #тут инциденты
    server_id = models.IntegerField()
    issue_type = models.CharField(max_length=50)
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Incident on server {self.server_id} - {self.issue_type}"


"""
Нужно создать три модели:
1) список серверов
2) данные которые будут сохраняться с этих серверов
3) таблица в которой будут храниться инциденты после проверки
"""