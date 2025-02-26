from cryptography.fernet import Fernet
import os

# Load the AES key
def load_key():
    with open("/Users/jesussolis/Downloads/capstone25/secret.key", "rb") as key_file:
        return key_file.read()

# Decrypt the file
def decrypt_file():
    key = load_key()
    cipher = Fernet(key)

    # Read encrypted file
    with open("hash_results.txt.enc", "rb") as file:
        encrypted_data = file.read()

    # Decrypt and restore original file
    decrypted_data = cipher.decrypt(encrypted_data)
    with open("hash_results.txt", "wb") as file:
        file.write(decrypted_data)

    # Remove encrypted file
    os.remove("hash_results.txt.enc")
    print("File decrypted and restored.")

# Run decryption
decrypt_file()
