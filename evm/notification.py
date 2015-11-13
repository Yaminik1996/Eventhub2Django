def send_notification(event, registration_ids):
	registration_ids = [id.encode('utf-8') for id in registration_ids]
	data = {}
	import json
	data['message'] = 'The event '+event.name+'\'s schedule has changed to '+event.date_time.strftime('%d/%m/%Y at %H:%M')
	fields = {'data':data, 'registration_ids' :registration_ids}
	headers = {'Authorization': 'key=AIzaSyCt1znpGShP057T3OhEUj_W8EG1wKETaSE','Content-Type': 'application/json' }
	print fields
	url = 'https://android.googleapis.com/gcm/send'
	import requests
	r = requests.post(url, data = json.dumps(fields), headers = headers)
	print r.content
	print r.status_code

if __name__ == "__main__":
	ids = ["APA91bGzrX6HEgdPg4XCI-30TE9gTg9YeUFayr7xb8KDDl6WbyzXBJhfNIzeadptI_pjcfRTMVpjdAVZraHIC9m6t_-9o6lEPp-hb13RyBBtN5MJmNzk-6bAme8OHI0TcTFH4yRu4nhD"]
	event = {}
	event["name"] = "Test event"
	event["date_time"] = "tomorrow"

	send_notification(event,ids)