from django.contrib.auth.models import AnonymousUser, User
from .models import *
from authentication.models import *
from .views import *
from django.test import TestCase, RequestFactory
import datetime
import json
# Create your tests here.



class addfollowing_test(TestCase):
	def setUp(self):
		self.factory = RequestFactory()
		self.user = AnonymousUser()

		#creating a user
		t = User(first_name = "test name", username = "makalaaneesh@yahoo.com", password = "vivek123", is_active = True)
		t.save()
		self.testuser = t
		profile = UserProfile()
		profile.user = self.testuser
		profile.mobile_id="test mobile id"
		profile.lastLoginDate = datetime.datetime.now()
		profile.ipaddress=""
		profile.save()
		self.profile = profile

		self.club1 = Club(name = "test club1", alias = "test club1")
		self.club1.save()
		self.club2 = Club(name = "test club2", alias = "test club2")
		self.club2.save()


	def test_correct_input(self):
		# post data to be sent
		data = {}
		data["email"] = self.testuser.username
		data["club_id"] = str(self.club1.id)+"|"+str(self.club2.id)
		data["club_id_unchecked"] =""
		# creating the request object
		request = self.factory.post("/followclub/",data = data)
		request.user = self.user
		# creating the response object 
		response = addfollowing(request)
		response = json.loads(response.content)
		#asserting the response back as success
		self.assertEqual(response["success"], 1)
		#asserting the correct functionality
		if data["club_id"] != '':
			club_ids = data['club_id'].split('|')
			follows = UserFollow.objects.filter(user__username = data['email'], club__id__in = club_ids)
			self.assertEqual(len(follows), len(club_ids))
		if data["club_id_unchecked"] != '':
			club_ids = data['club_id_unchecked'].split('|')
			unfollows = UserFollow.objects.filter(user__username = data['email'], club__id__in = club_ids)
			self.assertEqual(len(unfollows), 0)

