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
    
    master_password = "gAAAAABmIxE7SqgneY9zoETje7fEC8TKxfgrl2AbReJQVwBDLVBQDus6iRWDAheuAQPE8gagNi58IpKAaudkwGjAw3XUm2yjFoxrtX_cmIyAK1R7z7paZ1E="
    process_password = "gAAAAABmIxI_rMXi_iZsv8YWPl5BE6hdsmA1NOLYn_NuwiZv0fjKBLC1byKUbtWxCdeL4IszwrvPLDydKR9rs8bXRcdbo6jT0KHnDUBAhwbbtrf079JjOqQ="
    process_name = "create_text_number2.py"
    message = "Hello world 352!"
    
    Bowser_to_flask_app(master_password, process_password, process_name, message)