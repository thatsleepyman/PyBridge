from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import base64

def derive_encryption_key(password: str):
    """
    Derive a symmetric encryption key from a password.
    """
    password_bytes = password.encode()
    salt = b'salt_'  # CHANGE THIS - recommend using a key from os.urandom(16)
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
    )
    key = base64.urlsafe_b64encode(kdf.derive(password_bytes))
    return key

def encrypt_message(message: str, password: str):
    """
    Encrypt a message using a password.
    """
    key = derive_encryption_key(password)
    message_bytes = message.encode()
    fernet = Fernet(key)
    encrypted_message = fernet.encrypt(message_bytes)
    return encrypted_message.decode('utf-8')

def decrypt_message(encrypted_message: str, password: str):
    """
    Decrypt a message using a password.
    """
    key = derive_encryption_key(password)
    fernet = Fernet(key)
    decrypted_message = fernet.decrypt(encrypted_message.encode())
    return decrypted_message.decode('utf-8')

# Usage
encryption_password = 'B0ws3r_th3_3ncrypt10n_p4ssw0rd!'
message_to_encrypt = 'M45t3r_P455w0rd_1s_4w3s0m3!'

print('Encryption Password:', encryption_password)
encrypted_encryption_password = encrypt_message(encryption_password, encryption_password)
print('Encrypted Encryption Password:', encrypted_encryption_password)

print('Message to Encrypt:', message_to_encrypt)
encrypted_message = encrypt_message(message_to_encrypt, encryption_password)
print('Encrypted Message:', encrypted_message)