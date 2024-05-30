# Standard library imports
import requests


def api_request(MASTER_TOKEN, DEVELOPER_TOKEN, PYROCESS_TOKEN, PYROCESS_NAME, json_MESSAGE):
    url = f'http://127.0.0.1:5000/PyBridge/dev/{PYROCESS_NAME}'
    data = {'MASTER_TOKEN': MASTER_TOKEN,
            'DEVELOPER_TOKEN': DEVELOPER_TOKEN,
            'PYROCESS_TOKEN': PYROCESS_TOKEN,
            'json_MESSAGE': json_MESSAGE}
    response = requests.post(url, json=data)

    if response.status_code == 200:
        print(f"Status code: {response.status_code}\nResponse text: {response.text}")
    else:
        print(f"Status code: {response.status_code}\nResponse text: {response.text}")


if __name__ == '__main__':
    MASTER_TOKEN = "gAAAAABmWC2w38x80SOE57frQyEDkNyqL0YpATlU27XqDWk_oND9WrnmO6MQBU-RlaIXru5w5vkdjQa3_4wFvVkmWoUpeCmLzO7M_fojDi1_iU8IT6tgGEG0Gm-NwZOMO3rJxI7hl0FlmxHKZ1yDfDiYpWCSwHtYBQ=="
    DEVELOPER_TOKEN = "gAAAAABmWC5b3452haW9-si6gzPSGfanKNWFa6xSP02y11kbR39nZJeQAjN2Ymnm9dTxN8F4-d4C8tR35iTsoiEtpEaIlYlDsf4R8dsVTfFe9IJ_cEwdKa_NlEnJh1-MoSg5Q5uCnv7Z1Gv9PjXd4gqP7L2p0BRQnQ=="
    PYROCESS_TOKEN = "gAAAAABmWIpN7K5NOC1F1evxi7XeC2bXvATwkLYOfbEE2GFKXzmohhhtVnvAU0E7cwPYaahhyqCM7r9Auot_Zo1AZmBcQnQaww=="
    PYROCESS_NAME = "creator"
    json_MESSAGE = "Hello devver!"

    api_request(MASTER_TOKEN, DEVELOPER_TOKEN, PYROCESS_TOKEN, PYROCESS_NAME, json_MESSAGE)
