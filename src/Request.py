import requests

def Bowser_to_flask_app(MASTER_TOKEN, DEVELOPER_TOKEN, PROCESS_TOKEN, process_name, message):
    url = 'http://127.0.0.1:5000/Bowser_DEV'
    data = {'MASTER_TOKEN': MASTER_TOKEN,
            'DEVELOPER_TOKEN': DEVELOPER_TOKEN,
            'PROCESS_TOKEN': PROCESS_TOKEN,
            'process_name': process_name,
            'message': message}
    response = requests.post(url, json=data)
    
    if response.status_code == 200:
        print(f"Status code: {response.status_code}\nResponse text: {response.text}")
    else:
        print(f"Status code: {response.status_code}\nResponse text: {response.text}")


if __name__ == '__main__':
    
    MASTER_TOKEN = "MASTER_TOKEN_3002"
    DEVELOPER_TOKEN = "DEVELOPER_TOKEN_3002"
    PROCESS_TOKEN = "PROCESS_TOKEN_3002"
    process_name = "create_text_number3"
    message = "Hello world 3!"
    
    Bowser_to_flask_app(MASTER_TOKEN, DEVELOPER_TOKEN, PROCESS_TOKEN, process_name, message)