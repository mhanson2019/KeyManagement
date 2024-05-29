from key_handling import *
import getpass

programs = ["CDD_Vault", "SmartSheet"]

def main():
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
    save_encrypted_data('api_keys.bin', encrypted_data)
    print("API keys encrypted and saved to api_keys.bin")
    return key
    
if __name__ == "__main__":
    key = main()
    
    # test decryption of the api key file
    encrypted_data = load_encrypted_data('api_keys.bin')
    decrypted_data = decrypt_data(encrypted_data, key)
    print("Decrypted API keys:", eval(decrypted_data))