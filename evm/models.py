from django.db import models
from django.contrib.auth.models import User
# Create your models here.



def get_image_path(instance, filename):
    return '{0}{1}'.format(instance.event.alias,filename[filename.rfind("."):])





class Event(models.Model):
    TYPE_CHOICES = (
        ('event', 'event'),
        ('workshop', 'workshop'),
        ('lecture', 'lecture'),
        ('attraction', 'attraction'),
    )
    SUBTYPE_CHOICES = (
        ('general', 'general'),
        ('club', 'club'),
        ('IG', 'IG'),
        ('online', 'online'),
    )
    CLUB_CHOICES = (
        ('DND', 'DND'),
        ('music', 'music'),
        ('quiz', 'quiz'),
        ('DLD', 'DLD'),
    )


    type = models.CharField(max_length=128,choices=TYPE_CHOICES, default='event')
    subtype = models.CharField(max_length=128,choices=SUBTYPE_CHOICES, default='general')
    club = models.CharField(max_length=128,choices=CLUB_CHOICES, default='general')
    name = models.CharField(max_length=128)
    date_time = models.DateTimeField()
    contact_name_1 = models.CharField(max_length=128)
    contact_number_1 = models.CharField(max_length=10)
    contact_name_2 = models.CharField(max_length=128)
    contact_number_2 = models.CharField(max_length=10)
    venue = models.CharField(max_length=128)
    alias = models.CharField(max_length=128)
    addedby=models.ForeignKey(User, null=True, blank=True)
    def __unicode__(self):
		return self.name




class Content(models.Model):
    event = models.OneToOneField(Event, related_name='content')
    image = models.ImageField(upload_to=get_image_path, blank=True, null=True)
    description = models.TextField(max_length=128)
    addedby=models.ForeignKey(User, null=True, blank=True)
    def __unicode__(self):
		return self.event.name


class UserEvents(models.Model):
    event=models.ForeignKey(Event, related_name='event')
    user=models.ForeignKey(User,related_name='user')
    def __unicode__(self):
        return self.user.username

class EventRatings(models.Model):
    user=models.ForeignKey(User,related_name='userfeedback')
    event=models.ForeignKey(Event,related_name='eventfeedback')
    rating=models.IntegerField(default=0)
    feedback=models.TextField(max_length=300)
    def __unicode__(self):
        return self.user.username+" : "+self.event.name
        