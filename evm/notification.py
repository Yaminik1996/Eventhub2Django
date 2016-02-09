def send_notification(event, registration_ids):
	registration_ids = [id.encode('utf-8') for id in registration_ids]
	data = {}
	import json
	# data['message'] = 'test notif'
	data['message'] = 'The event '+event.name+'\'s schedule has changed to '+event.date_time.strftime('%d/%m/%Y at %H:%M') +' at '+event.venue
	fields = {'data':data, 'registration_ids' :registration_ids}
	headers = {'Authorization': 'key=AIzaSyDjYk4nCrXn6Nb2VL2EZgGbebT7NdLJ5s8','Content-Type': 'application/json' }
	print fields
	url = 'https://android.googleapis.com/gcm/send'
	import requests
	r = requests.post(url, data = json.dumps(fields), headers = headers)
	print r.content
	print r.status_code


def send_notification_custom(event, registration_ids, message):
	registration_ids = [id.encode('utf-8') for id in registration_ids]
	data = {}
	import json
	data['message'] = message
	# data['message'] = 'The event '+event.name+'\'s schedule has changed to '+event.date_time.strftime('%d/%m/%Y at %H:%M') +' at '+event.venue
	fields = {'data':data, 'registration_ids' :registration_ids}
	headers = {'Authorization': 'key=AIzaSyDjYk4nCrXn6Nb2VL2EZgGbebT7NdLJ5s8','Content-Type': 'application/json' }
	print fields
	url = 'https://android.googleapis.com/gcm/send'
	import requests
	r = requests.post(url, data = json.dumps(fields), headers = headers)
	print r.content
	print r.status_code


def send_event(event, image_url, registration_ids):
	'''
	Using this function as a means to update events in the app's local db by sending event details using android gcm
	'''
	registration_ids = [id.encode('utf-8') for id in registration_ids]
	data = {}
	import json
	data['message'] = "A new event has been added!"
	data['id'] = event.id
	data['type'] = event.type
	data['subtype'] = event.subtype
	data['name'] = event.name
	data['content'] = event.content
	data['description'] = event.description
	data['cname1'] = event.contact_name_1
	data['cname2'] = event.contact_name_2
	data['cno1'] = event.contact_number_1
	data['cno2'] = event.contact_number_2
	data['club'] = event.club.name
	data['image'] = image_url
	data['date_time'] = event.date_time


	fields = {'data':data, 'registration_ids' :registration_ids}
	headers = {'Authorization': 'key=AIzaSyDjYk4nCrXn6Nb2VL2EZgGbebT7NdLJ5s8','Content-Type': 'application/json' }
	print fields
	url = 'https://android.googleapis.com/gcm/send'
	import requests
	r = requests.post(url, data = json.dumps(fields), headers = headers)
	print r.content
	print r.status_code

if __name__ == "__main__":
	ids = ["APA91bGCS2kkPIHgjqmBhI5YW3TZaVJCGi3fxdlKcE4oA6USULcreEcdJIbRSsFGpqL8joRqa2Vzia5rEJUjJqwF69Xb5vp1W-HQNoLcSxh0d-z0NNRvgaQtGLxwHCmY9ldx5qrAJpo5EeoZ1zrypObXUza28MywLw"]
	# ids = ["APA91bHEJIIqZZgZZ7RrAaI27d7-p3hrf5CUUNn6wq6V2TYSbAapOwTiTGOCIqYl4vmcuqI-Ux0ruypydm-ZqZO5qkqT4e4s4Zn2jv_6utzFDpAc5MTFuj-FarnMhzAqThe5c6QBxQwn"]
	event = {}
	event["name"] = "Test event"
	event["date_time"] = "tomorrow"

	send_notification_custom(event,ids,"This is a test notification")