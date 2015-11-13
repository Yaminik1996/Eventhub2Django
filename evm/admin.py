from django.contrib import admin
from .models import Event, Content, UserEvents, EventRatings
import notification
# Register your models here.


class EventAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
    	if 'date_time' in form.changed_data or 'venue' in form.changed_data:
    		users = UserEvents.objects.values_list('user__userprofile__mobile_id', flat=True).filter(event = obj)
    		print "list is------------------------ ",users
    		ids = users
    		# ids = ["APA91bGzrX6HEgdPg4XCI-30TE9gTg9YeUFayr7xb8KDDl6WbyzXBJhfNIzeadptI_pjcfRTMVpjdAVZraHIC9m6t_-9o6lEPp-hb13RyBBtN5MJmNzk-6bAme8OHI0TcTFH4yRu4nhD"]
    		if len(ids) > 0:
    			notification.send_notification(obj,ids)
		return super(EventAdmin, self).save_model(request, obj, form, change)

admin.site.register(Event, EventAdmin)
admin.site.register(Content)
admin.site.register(UserEvents)
admin.site.register(EventRatings)
