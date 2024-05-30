# Standard library imports
import requests


def api_request(MASTER_TOKEN, PROCESS_TOKEN, process_name, message):
    url = 'http://127.0.0.1:5000/PyBridge'
    data = {'MASTER_TOKEN': MASTER_TOKEN,
            'PROCESS_TOKEN': PROCESS_TOKEN,
            'process_name': process_name,
            'message': message}
    response = requests.post(url, json=data)

    if response.status_code == 200:
        print(f"Status code: {response.status_code}\nResponse text: {response.text}")
    else:
        print(f"Status code: {response.status_code}\nResponse text: {response.text}")


if __name__ == '__main__':
    MASTER_TOKEN = "gAAAAABmWC2w38x80SOE57frQyEDkNyqL0YpATlU27XqDWk_oND9WrnmO6MQBU-RlaIXru5w5vkdjQa3_4wFvVkmWoUpeCmLzO7M_fojDi1_iU8IT6tgGEG0Gm-NwZOMO3rJxI7hl0FlmxHKZ1yDfDiYpWCSwHtYBQ=="
    PROCESS_TOKEN = "gAAAAABmWC7AY5Ajea54eI1R58x427HC7y-HrSj5tOcFsTWtvYQEs1Pdn86uEzANteSzKOjHUuZHs9pOjuNtvxYmfQprkfz6tk2RGkVPESiixkXxmqeWzHMznl0mbucdUUCcTRESVN8XvgHccfuKtXzTZvw8IGGrLQ=="
    process_name = "creator"
    message = "Hello world 37!"

    api_request(MASTER_TOKEN, PROCESS_TOKEN, process_name, message)
