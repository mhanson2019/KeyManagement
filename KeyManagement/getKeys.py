from key_handling import *
import argparse
import getpass

apiFile = 'api_keys.bin'

# set up argparse for passing in the
def parse_args():
    parser = argparse.ArgumentParser(description="Decrypt API keys")
    parser.add_argument(
        "-k",
        "--key",
        help="Key to decrypt the API keys",
        required=False,
    )
    return parser.parse_args()


def main(key = None):
    if key is None:
        
        # Use getpass to ask for the key derived from the original passcode
        key = getpass.getpass("Enter the key: ")
    
    # Load the encrypted api keys from the file
    encrypted_data = load_encrypted_data(apiFile)
    
    # Decrypt the api keys
    decrypted_data = decrypt_data(encrypted_data, key)
    
    return eval(decrypted_data)

if __name__ == "__main__":
    args = parse_args()
    api_keys = main(args.key)
    
    print("API keys:", api_keys)