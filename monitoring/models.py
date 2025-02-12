from django.db import models

class Machine(models.Model): # инфо о серверах
    name = models.CharField(max_length=100, unique=True)
    ip_address = models.GenericIPAddressField(unique=True)

    def __str__(self):
        return self.name

class ResourceUsage(models.Model): # данные загрузки каждого сервера
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE)
    cpu = models.FloatField()
    mem = models.FloatField()
    disk = models.FloatField()
    uptime = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)

class Incident(models.Model): # содержит в себе опасные сервера
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE)
    resource = models.CharField(max_length=10)
    value = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)


"""
Нужно создать три модели:
1) список серверов
2) данные которые будут сохраняться с этих серверов
3) таблица в которой будут храниться инциденты после проверки
"""