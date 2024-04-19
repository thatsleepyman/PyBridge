import requests

def Bowser_to_flask_app(master_password, process_password, process_name, message):
    url = 'http://127.0.0.1:5000/Bowser'
    data = {'master_password': master_password,
            'process_password': process_password,
            'process_name': process_name,
            'message': message}
    response = requests.post(url, json=data)
    
    if response.status_code == 200:
        print(f"Status code: {response.status_code}\nResponse text: {response.text}")
    else:
        print(f"Status code: {response.status_code}\nResponse text: {response.text}")


if __name__ == '__main__':
    
    master_password = "M@sterPassw0rd!"
    process_password = "passw0rd2!"
    process_name = "create_text.py"
    message = "Hello world 112!"
    
    Bowser_to_flask_app(master_password, process_password, process_name, message)