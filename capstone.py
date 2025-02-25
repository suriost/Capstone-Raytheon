import hashlib
import datetime

# harcoded input string
text = "asu"

#collecting user input
hash_input = input("Hash This: ")

# 1 to encrypt or 2 to decrypt
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

    # Printing the final result to the console
    print(f"MD5 Hash: {current_hash}")
    print("Hash saved")

elif hash_decision == 2:
    # decryption()
    pass
else:
    invalid()