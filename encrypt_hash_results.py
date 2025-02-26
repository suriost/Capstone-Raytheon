from cryptography.fernet import Fernet
import os

# Load the AES key
def load_key():
    with open("/Users/jesussolis/Downloads/capstone25/secret.key", "rb") as key_file:
        return key_file.read()

# Encrypt the file
def encrypt_file():
    key = load_key()
    cipher = Fernet(key)

    # Read plaintext file
    with open("hash_results.txt", "rb") as file:
        file_data = file.read()

    # Encrypt and save as new file
    encrypted_data = cipher.encrypt(file_data)
    with open("hash_results.txt.enc", "wb") as file:
        file.write(encrypted_data)

    # Delete the original file to prevent writing to it
    os.remove("hash_results.txt")
    print("File encrypted and original deleted.")

# Run encryption
encrypt_file()
