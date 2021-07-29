import json
import requests # htttp requests

BASE_URL = "http://127.0.0.1:8000/"
ENDPOINT = "api/updates/"


def get_list(id = None):
	data = json.dumps({})
	if id is not None:
		data = json.dumps({
			"id":id
		})
	r = requests.get(BASE_URL + ENDPOINT, data = data)
	print(r.status_code)
	data = r.json()
	return data

def create_update():
	new_data = {
		'user': 1,
		'content' : "another new cool updates",
	}
	r = requests.post(BASE_URL + ENDPOINT , data = json.dumps(new_data))
	# print(r.headers)
	print(r.status_code)
	if r.status_code == requests.codes.ok:
		return r.json()

	return r.text


def do_obj_update():
	new_data = {
		"id": 12,
		"content" : "awsome data",
	}
	r = requests.put(BASE_URL + ENDPOINT, data = json.dumps(new_data))
	# print(r.headers)
	print(r.status_code)
	if r.status_code == requests.codes.ok:
		return r.json()

	return r.text


def do_obj_delete():
	new_data = {
		"id": 12,
		"content" : "New obj data",
	}
	r = requests.delete(BASE_URL + ENDPOINT, data = json.dumps(new_data))
	# print(r.headers)
	print(r.status_code)
	if r.status_code == requests.codes.ok:
		return r.json()

	return r.text

# print(create_update())
print(get_list())
# print(do_obj_update())
# print(do_obj_delete())