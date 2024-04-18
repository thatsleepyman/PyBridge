import requests

def send_to_writer(message):
    url = 'http://127.0.0.1:5000/send_to_writer'
    data = {'message': message}
    response = requests.post(url, data=data)
    return response.text
