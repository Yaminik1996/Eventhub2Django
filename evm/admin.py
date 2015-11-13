from django.contrib import admin
from .models import Event, Content, UserEvents, EventRatings
# Register your models here.

admin.site.register(Event)
admin.site.register(Content)
admin.site.register(UserEvents)
admin.site.register(EventRatings)