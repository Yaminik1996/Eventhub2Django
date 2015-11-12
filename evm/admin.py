from django.contrib import admin
from .models import Event, Content, UserEvents
# Register your models here.

admin.site.register(Event)
admin.site.register(Content)
admin.site.register(UserEvents)