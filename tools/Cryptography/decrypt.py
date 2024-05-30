from cryptography.fernet import Fernet


def decrypt_password(encrypted_password, encryption_key):
    # Ensure the key is 32 bytes and URL-safe base64-encoded
    key = encryption_key.encode('utf-8')
    cipher_suite = Fernet(key)

    # Decrypt the password
    decrypted_password = cipher_suite.decrypt(encrypted_password).decode('utf-8')

    return decrypted_password


def main():
    # Get input from the user
    to_be_decrypted = "gAAAAABmWC7AY5Ajea54eI1R58x427HC7y-HrSj5tOcFsTWtvYQEs1Pdn86uEzANteSzKOjHUuZHs9pOjuNtvxYmfQprkfz6tk2RGkVPESiixkXxmqeWzHMznl0mbucdUUCcTRESVN8XvgHccfuKtXzTZvw8IGGrLQ=="
    encryption_key = "mRl_Z5IfvcfhV-keSLXiAslYQI2Qa23X1Ru2jHoptoM="

    # Convert the base64-encoded string to bytes
    encrypted_password = to_be_decrypted.encode('utf-8')

    # Decrypt the password
    decrypted_password = decrypt_password(encrypted_password, encryption_key)

    # Print the decrypted password
    print("Decrypted Password:", decrypted_password)


if __name__ == "__main__":
    main()
