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

if __name__ == "__main__":
	ids = ["APA91bHEJIIqZZgZZ7RrAaI27d7-p3hrf5CUUNn6wq6V2TYSbAapOwTiTGOCIqYl4vmcuqI-Ux0ruypydm-ZqZO5qkqT4e4s4Zn2jv_6utzFDpAc5MTFuj-FarnMhzAqThe5c6QBxQwn"]
	event = {}
	event["name"] = "Test event"
	event["date_time"] = "tomorrow"

	send_notification(event,ids)