# django-monitoring-service

### 1 Клонирование 
##### Клонируйте себе репозиторий 
```git clone <https://github.com/sxd0/django-monitoring-service.git>```


### 2 Докер
##### Приложение запускается докером. Команда прописывается в корне
```docker-compose up --build```
##### Далее нужно подождать пока все сервисы запустятся

### 3 Ожидание и просмотр
##### Как только видны таски(к примеру fetch_server_data) можно идти проверять добавление в базу данных ресурсов и инцидентов
##### обычно это будет вот так
```celery-beat-1  | [2025-02-13 18:15:00,011: INFO/MainProcess] Scheduler: Sending due task fetch-server-data-every-15-minutes (monitoring.tasks.fetch_server_data)
celery-beat-1  | [2025-02-13 18:15:00,030: INFO/MainProcess] Scheduler: Sending due task monitor-resources-every-15-minutes (monitoring.tasks.monitor_resources)
```

##### открыть новый терминал и ввести команды
```docker-compose exec db mysql -u root -p```
```пароль "12345"```
##### Далее для просмотра достаточно будет ввести следующие команды
```use monitoring_db```
```select * from monitoring_serverresource;``` - (для просмотра всех метрик) и ```select * from monitoring_incident``` - (для просмотра инцидентов)

### Есть второй вариант просмотреть в удобном интерфейсе бд
##### Введите эту команду для создания суперюзера
```docker-compose exec web python manage.py createsuperuser``` 
и далее перейти по адресу со своими параметрами
##### http://localhost:8000/admin


### заглушка тоже на django
### для задач использовал celery+redis


