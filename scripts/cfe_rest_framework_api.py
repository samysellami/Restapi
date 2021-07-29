import requests
import json
import os

AUTH_ENDPOINT = "http://127.0.0.1:8000/api/auth/"  
REFRESH_ENDPOINT = AUTH_ENDPOINT + "refresh/"  
image_path = os.path.join(os.getcwd(), "logo.png")

headers = {
	"Content-Type": "application/json",
}

data = {
	'username': 'admin',
	'password': 'requiem',
}

r = requests.post(AUTH_ENDPOINT, data = json.dumps(data), headers = headers)
token = r.json()['token']
print(token)

BASE_ENDPOINT = "http://127.0.0.1:8000/api/status/"
ENDPOINT =  BASE_ENDPOINT + "12/"
headers2 = {
	# "Content-Type": "application/json",
	"Authorization": 'JWT ' + token  
}

data2 = {
	'content': "new content post"
}

with open(image_path, 'rb') as image:
	file_data = {
		'image': image
	}
	r = requests.get(ENDPOINT, headers = headers2)
	# r = requests.put(ENDPOINT, data = data2, files = file_data, headers = headers2)
	# r = requests.post(BASE_ENDPOINT, data = data2, files = file_data, headers = headers2)
	print(r.text)







# AUTH_ENDPOINT = "http://127.0.0.1:8000/api/auth/register/"  
# REFRESH_ENDPOINT = AUTH_ENDPOINT + "refresh/"  
# ENDPOINT = "http://127.0.0.1:8000/api/status/"

# image_path = os.path.join(os.getcwd(), "logo.png")

# headers = {
# 	"Content-Type": "application/json",
# 	"Authorization": "JWT " + 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxMSwidXNlcm5hbWUiOiJzYW15MTEiLCJleHAiOjE2MjY3ODg3MDMsImVtYWlsIjoiczExLnNlbGxhbWlAaW5ub3BvbGlzLnVudmllcnNpdHkiLCJvcmlnX2lhdCI6MTYyNjc4ODQwM30.XObqF2Xhja8dSsZU_tZ1CfeiLnJH0hqN-Rh0OraHkX4'
# }

# data = {
# 	'username': 'samy11',
# 	'email': 's11.sellami@innopolis.unviersity',
# 	'password': 'requiem',
# 	'password2': 'requiem'
# }

# r = requests.post(AUTH_ENDPOINT, data = json.dumps(data), headers = headers)
# token = r.json()#['token']
# print(token)




















# refresh_data = {
# 	'token': token,
# }
# new_r = requests.post(REFRESH_ENDPOINT, data = json.dumps(refresh_data), headers = headers)
# new_token = new_r.json()#['token']
# print(new_token)

# get_endpoint = ENDPOINT + str(12)
# r = requests.get(get_endpoint)
# print(r.text)
# r2 = requests.get(ENDPOINT)
# print(r2.status_code)


# post_headers = {
# 	# 'Content-Type': 'application/json',
# 	"Authorization": "JWT " + token
# }
# with open(image_path, 'rb') as image:
# 	file_data = {
# 		'image': image
# 	}
# 	data = {
# 		"content": "updated description "
# 	}
# 	json_data =json.dumps(data) 
# 	posted_response = requests.put(ENDPOINT + str(12) + '/', data = data, headers = post_headers, files = file_data)
# 	print(posted_response.text)


# post_headers = {
# 	# 'Content-Type': 'application/json',
# 	"Authorization": "JWT " + token
# }
# data = {
# 	"content": "updated description "
# }
# json_data =json.dumps(data) 
# posted_response = requests.put(ENDPOINT + str(12) + '/', data = data, headers = post_headers)
# print(posted_response.text)


















# def do_img(method = 'get', data = {}, is_json = True, img_path = None):
# 	headers = {}
# 	if is_json:
# 		headers['content-type'] = 'application/json'
# 		data = json.dumps(data)
# 	if img_path is not None:
# 		with open(image_path, 'rb') as image:
# 			file_data = {
# 				'image': image
# 			}
# 			r = requests.request(method, ENDPOINT, data = data, files = file_data, headers = headers)
# 	else:
# 		r = requests.request(method, ENDPOINT, data = data, headers = headers)
# 	print(r.text)
# 	print(r.status_code)
# 	return r


# def do(method = 'get', data = {}, is_json = True):
# 	headers = {}
# 	if is_json:
# 		headers['content-type'] = 'application/json'
# 		data = json.dumps(data)
# 	r = requests.request(method, ENDPOINT, data = data, headers = headers)
# 	print(r.text)
# 	print(r.status_code)
# 	return r

# do(data = {'id':3}) 
# do(method = 'post', data = {"content": "some new cool content"}) 
# do(method = 'delete', data = {'id':7})
# do(method = 'put', data = {'id':3, 'content': "some new content", 'user': 1})
# do_img(
# 	method = 'put', 
# 	data= {'id': 9, 'user': 1, "content":"Some new content"}, 
# 	is_json = False, 
# 	img_path = image_path
# )