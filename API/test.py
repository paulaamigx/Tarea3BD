import requests
import json

#response = requests.put('http://127.0.0.1:5000/api/users/1') 
data = {
					'username'	: 'uu',
					'surname'		: 'ss',
					'email'			: 'ee',
					'password'	: 'pp',
					'country'		:	1
			 }
data = json.dumps(data, indent=4)
response = requests.post('http://127.0.0.1:5000/api/users', data=data)
print(response.text)
