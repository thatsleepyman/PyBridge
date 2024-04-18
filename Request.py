import requests

url = 'http://127.0.0.1:5000/send_to_writer'
data = {'message': 'Hello world'}

response = requests.post(url, data=data)

print(response.text)