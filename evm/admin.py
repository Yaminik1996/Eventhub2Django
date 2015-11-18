from django.contrib import admin
from .models import Event, Content, UserEvents, EventRatings
import notification
from django.http import HttpResponseRedirect,JsonResponse,HttpResponse
# Register your models here.


class EventAdmin(admin.ModelAdmin):
	exclude = ('addedby',)
	def get_queryset(self,request):
		print "Check"
		queryset = super(EventAdmin, self).get_queryset(request)
		if request.user.is_superuser:
			print "Super user"
			return queryset
		else:
			print "Normal"
			return queryset.filter(addedby=request.user)
	def save_model(self, request, obj, form, change):
		if getattr(obj, 'addedby', None) is None:
			print "None"
			obj.addedby = request.user
			obj.save()
		if 'date_time' in form.changed_data or 'venue' in form.changed_data:
			users = UserEvents.objects.values_list('user__userprofile__mobile_id', flat=True).filter(event = obj)
			print "list is------------------------ ",users
			ids = users
			# ids = ["APA91bGzrX6HEgdPg4XCI-30TE9gTg9YeUFayr7xb8KDDl6WbyzXBJhfNIzeadptI_pjcfRTMVpjdAVZraHIC9m6t_-9o6lEPp-hb13RyBBtN5MJmNzk-6bAme8OHI0TcTFH4yRu4nhD"]
			if len(ids) > 0:
				notification.send_notification(obj,ids)
		return super(EventAdmin, self).save_model(request, obj, form, change)
	def response_add(self, request, obj, post_url_continue=None):
		return HttpResponseRedirect("/admin/evm/content/add/")


class ContentAdmin(admin.ModelAdmin):
	exclude=('addedby',)
	def get_queryset(self,request):
		print "Check"
		queryset = super(ContentAdmin, self).get_queryset(request)
		if request.user.is_superuser:
			print "Super user"
			return queryset
		else:
			print "Normal"
			return queryset.filter(addedby=request.user)
	def save_model(self, request, obj, form, change):
		if getattr(obj, 'addedby', None) is None:
			print "None"
			obj.addedby = request.user
			obj.save()


admin.site.register(Event, EventAdmin)
admin.site.register(Content, ContentAdmin)
admin.site.register(UserEvents)
admin.site.register(EventRatings)
