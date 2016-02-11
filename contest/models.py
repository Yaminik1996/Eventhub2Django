from django.db import models

# Create your models here.



class SectionScore(models.Model):
	section=models.CharField(max_length=200)
	rollno=models.CharField(max_length=200,null=True)
	email=models.CharField(max_length=200,null=True)
	number=models.CharField(max_length=200,null=True)
	is_android=models.BooleanField(default=True)
	is_download=models.BooleanField(default=False)
	def __unicode__(self):
		return self.section+" : "+self.email

