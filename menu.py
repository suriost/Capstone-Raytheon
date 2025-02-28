# main menu
import subprocess
import time
from logger import log_error

def print_hline():
    """ Prints a Horizontal Line """
    print("-" * 80)


def print_menu():
    """ Pretty prints menu and user prompt """
    # title
    print_hline()
    print("\n\t\t\tRaytheon Security\n")
    print_hline()

    # prompts
    print_hline()
    print("1. Generate Key")
    print("2. Encrypt File")
    print("3. Decrypt File")
    print("4. Capstone.py Example")
    print("5. Exit")


def run_task(command):
    try:
        result = subprocess.run(command, shell=True, check=True) #, capture_output=True, text=True)
        return result.stdout
    except subprocess.CallProcessError as e:
        log_error("Task Failed", f"Command: {command}, Error {e}", alert=True )
        print(f"Error: {e}")

def handle_input():
    curr_input = input("> ").strip()

    match curr_input:
        case "1":
            print("Generating...")
            run_task("python gen_key.py")
        case "2":
            print("Encrypting...")
            run_task("python encrypt_hash_results.py")
        case "3":
            print("Decrypting...")
            run_task("python decrypt_hash_results.py")
        case "4":
            run_task("python capstone.py")
        case "5":
            print("Exiting program")
            exit(0)
        case _:
            print("Invalid input, please try again")


def main():
    """
    tasks = [
        "python x.py",
    ]
    """

    while True:    
        #for task in tasks
        print_menu()
        handle_input()

main()