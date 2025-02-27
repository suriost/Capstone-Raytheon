# main menu
import subprocess

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


def handle_input():
    curr_input = input("> ").strip()

    match curr_input:
        case "1":
            print("Generating...")
            subprocess.run(["python", "gen_key.py"])
        case "2":
            print("Encrypting...")
            subprocess.run(["python", "encrypt_hash_results.py"])
        case "3":
            print("Decrypting...")
            subprocess.run(["python", "decrypt_hash_results.py"])
        case "4":
            subprocess.run(["python", "capstone.py"])


def main():
    while True:    
        print_menu()
        handle_input()

main()