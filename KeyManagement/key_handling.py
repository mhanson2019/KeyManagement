from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import base64
import os

def generate_salt():
    """Generate a salt for key derivation"""
    return os.urandom(16)

def derive_key(passcode, salt):
    """Derive a key from the given passcode and salt"""
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
    )
    key = base64.urlsafe_b64encode(kdf.derive(passcode.encode()))
    return key

def encrypt_data(data, key):
    """Encrypt the given data using the provided key"""
    fernet = Fernet(key)
    encrypted_data = fernet.encrypt(data)
    return encrypted_data

def decrypt_data(encrypted_data, key):
    """Decrypt the encrypted data using the provided key"""
    fernet = Fernet(key)
    decrypt_data = fernet.decrypt(encrypted_data)
    return decrypt_data.decode()

def save_encrypted_data(file_path, encrypted_data):
    """Save the encrypted data to a file"""
    with open(file_path, 'wb') as file:
        file.write(encrypted_data)

def load_encrypted_data(file_path):
    """Load the encrypted data from a file"""
    with open(file_path, 'rb') as file:
        encrypted_data = file.read()
    return encrypted_data