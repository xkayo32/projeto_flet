from cryptography.fernet import Fernet
from decouple import config


def encrypt_key(string: str):
    key = config('KEY_ENCRYPT')
    f = Fernet(key)
    return f.encrypt(string.encode())


def decrypt_key(string: str):
    key = config('KEY_ENCRYPT')
    f = Fernet(key)
    return f.decrypt(string.encode())
