import hashlib
import datetime
import os

# check if hash_results.txt is decrypted
def is_decrypted():
    if not os.path.exists("hash_results.txt"):
        # message to display if it is not found
        print("hash_results.txt not found.")
        return False
    
    try:
        with open("hash_results.txt", "r") as file:
            content = file.read(100)  # Read a small portion to check
            if "Error: Invalid option" in content or "MD5 Hash:" in content:
                return True
    except Exception as e:
        print(f"Error reading file: {e}")
    
    print("hash_results.txt appears to be encrypted or unreadable.")
    return False

# we will exit the program if hahs_results.txt is not decrypted
if not is_decrypted():
    exit()

# collecting user input
hash_input = input("Hash This: ")

# 4720 to encrypt
hash_decision = int(input("Enter your choice: "))

def encryption(hash_input):
    # create the MD5 hash object
    md5_hash = hashlib.md5()

    # update the hash object with the string
    md5_hash.update(hash_input.encode('utf-8'))

    # get the hexadecimal representation of the hash
    hash_result = md5_hash.hexdigest()

    # Return the result of the hash
    return hash_result

'''
def decryption():
    # Ask for the hash to "decrypt"
    hash_to_decrypt = input("Enter the MD5 hash to decrypt: ")

    # Check if the hash exists in the stored dictionary
    if hash_to_decrypt in stored_hashes:
        print(f"The original text for the hash {hash_to_decrypt} is: {stored_hashes[hash_to_decrypt]}")
    else:
        print("No match found for the provided hash.")
'''

def invalid():
    # code to get the current timestamp
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # writing into a file
    with open("hash_results.txt", "a") as file:
        file.write(f"{timestamp} - Error: Invalid option, choose to encrypt or decrypt\n")
        file.write("\n")

if hash_decision == 1:
    current_hash = hash_input

    # Loop to perform hashing 3 times
    for i in range(3):
        # Perform the hashing
        current_hash = encryption(current_hash)

    # Code to get the current timestamp
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Writing the final result into the file
    with open("hash_results.txt", "a") as file:
        file.write(f"{timestamp} - MD5 Hash: {current_hash}\n")
        file.write("\n")

elif hash_decision == 2:
    # decryption()
    pass
else:
    invalid()
    print("Error found: Invalid Option")
