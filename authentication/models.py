from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    collegeName = models.CharField(max_length=128)
    signUpDate = models.DateField(auto_now=True)
    ipaddress = models.URLField(max_length=25)
    lastLoginDate = models.DateTimeField(blank=True)
    def __unicode__(self):
    	return self.user.first_name