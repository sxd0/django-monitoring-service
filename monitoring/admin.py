from django.contrib import admin

from monitoring.models import Incident, ServerResource

# Register your models here.
admin.site.register(ServerResource)
admin.site.register(Incident)