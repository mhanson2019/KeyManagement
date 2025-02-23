from .key_handling import *
import getpass
import argparse
import json

programs = ["CDD_Vault", "SmartSheet"]

# set up argparse for passing in the
def parse_args():
    parser = argparse.ArgumentParser(description="Encrypt API keys with optional name of the file to save to")
    parser.add_argument(
        "-n",
        "--name",
        help="Name of the file to save the encrypted API keys",
        defaault="api_keys.bin",
        required=False,
    )
    return parser.parse_args()

def main(filename):
    if filename != "api_keys.bin":
        print("Saving encrypted API keys to", filename)
    # read the programs list from a json file
    with open('programs.json', 'r') as f:
        programs = json.load(f)
    
    # Use getpass to ask for the passcode
    passcode = getpass.getpass("Enter a passcode: ")
    
    # Generate a salt and derive a key from the passcode
    salt = generate_salt()
    key = derive_key(passcode, salt)
    
    # Print the key with instructions to save in password manager
    print("Key:", key.decode())
    print("Save this key in your password manager")
    
    # User inquirer to ask for the api key for each program in programs list and store in a dictionary
    api_keys = {}
    for program in programs:
        api_key = getpass.getpass(f"Enter the API key for {program}: ")
        api_keys[program] = api_key
        # print stored api key to confirm integrity
        print(f"API key for {program}:", api_keys[program])
    
    # Encrypt the api keys and save to a file
    encrypted_data = encrypt_data(str(api_keys).encode(), key)
    save_encrypted_data(filename, encrypted_data)
    print(f"API keys encrypted and saved to {filename}")
    return key
    
if __name__ == "__main__":
    args = parse_args()
    key = main(args.name)
    
    # test decryption of the api key file
    encrypted_data = load_encrypted_data('api_keys.bin')
    decrypted_data = decrypt_data(encrypted_data, key)
    print("Decrypted API keys:", eval(decrypted_data))