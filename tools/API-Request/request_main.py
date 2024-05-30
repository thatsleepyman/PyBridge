# Standard library imports
import requests


def api_request(MASTER_TOKEN, USER_TOKEN, PYROCESS_TOKEN, PYROCESS_NAME, json_MESSAGE):
    url = f'http://127.0.0.1:5000/PyBridge/main/{PYROCESS_NAME}'
    data = {'MASTER_TOKEN': MASTER_TOKEN,
            'USER_TOKEN': USER_TOKEN,
            'PYROCESS_TOKEN': PYROCESS_TOKEN,
            'json_MESSAGE': json_MESSAGE}
    response = requests.post(url, json=data)

    if response.status_code == 200:
        print(f"Status code: {response.status_code}\nResponse text: {response.text}")
    else:
        print(f"Status code: {response.status_code}\nResponse text: {response.text}")


if __name__ == '__main__':
    MASTER_TOKEN = "gAAAAABmWC2w38x80SOE57frQyEDkNyqL0YpATlU27XqDWk_oND9WrnmO6MQBU-RlaIXru5w5vkdjQa3_4wFvVkmWoUpeCmLzO7M_fojDi1_iU8IT6tgGEG0Gm-NwZOMO3rJxI7hl0FlmxHKZ1yDfDiYpWCSwHtYBQ=="
    USER_TOKEN = "gAAAAABmWI9XTVbu7PVRPiL2cGTEUcqVrywFU-nTX_mUoZ3O5_Po7yFJVnRjPJILlOGIChqoJmsKKd-ZT3d_alxv2sAqfkUqaFaHaUPiDCUM69L3-nmsb9ujQh4Zv5JOe5VHl_Wc9XnBlXr4Jv7b_-TKu5T0IRrNhA=="
    PYROCESS_TOKEN = "gAAAAABmWIp6ProXZageqcwdzqgZIyDVrTpZqDPty5x5TkkRuZuFXAsguYuK0OoUkh1h3JuWROFBheO3PmFmSg_pwzo1V4Gbpg=="
    PYROCESS_NAME = "creator"
    json_MESSAGE = "Hello main-world :)!"

    api_request(MASTER_TOKEN, USER_TOKEN, PYROCESS_TOKEN, PYROCESS_NAME, json_MESSAGE)
