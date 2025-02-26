from cryptography.fernet import Fernet

# Generate AES key
key = Fernet.generate_key()

# Save the key to a file
with open("secret.key", "wb") as key_file:
    key_file.write(key)

print("Secret key generated and saved.")
