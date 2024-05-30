import secrets
import base64


def generate_key(length):
    # Generate a random key of the specified length
    key = secrets.token_bytes(length)
    # Convert the key to a URL-safe base64-encoded string
    key = base64.urlsafe_b64encode(key)
    return key.decode('utf-8')


print(generate_key(32))  # Generate a 32-byte key
