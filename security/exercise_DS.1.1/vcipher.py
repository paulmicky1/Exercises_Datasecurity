'''
	vcipher.py

	Copyright (c) PAUL MICKY D COSTA
	Licensed under the MIT license: https://opensource.org/license/mit
'''
def vigE(key, cleartext):
    """
    Encrypt the cleartext using the Vigenère Cipher with the given key.
    
    Parameters:
    key (str): The encryption key (a non-empty string).
    cleartext (str): The text to be encrypted (a non-empty string).
    
    Returns:
    str: The encrypted ciphertext.
    """
    ciphertext = ""
    key_length = len(key)
    
    for i, char in enumerate(cleartext):
        if char.isalpha():
            shift = ord(key[i % key_length].lower()) - 97  # Get shift based on key character
            if char.isupper():
                ciphertext += chr((ord(char) - 65 + shift) % 26 + 65)
            else:
                ciphertext += chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            # Non-alphabetic characters are not changed
            ciphertext += char
            
    return ciphertext


def vigD(key, ciphertext):
    """
    Decrypt the ciphertext using the Vigenère Cipher with the given key.
    
    Parameters:
    key (str): The decryption key (a non-empty string).
    ciphertext (str): The text to be decrypted (a non-empty string).
    
    Returns:
    str: The decrypted plaintext.
    """
    plaintext = ""
    key_length = len(key)
    
    for i, char in enumerate(ciphertext):
        if char.isalpha():
            shift = ord(key[i % key_length].lower()) - 97  # Get shift based on key character
            if char.isupper():
                plaintext += chr((ord(char) - 65 - shift) % 26 + 65)
            else:
                plaintext += chr((ord(char) - 97 - shift) % 26 + 97)
        else:
            # Non-alphabetic characters are not changed
            plaintext += char
            
    return plaintext


# Main program to interact with the user
if __name__ == "__main__":
    # Take user input for the key (must be non-empty string)
    key = input("Enter the Vigenère Cipher key (non-empty string): ")
    while len(key) == 0:
        key = input("The key cannot be empty. Please enter the key again: ")

    # Take user input for the cleartext (must be non-empty string)
    cleartext = input("Enter the cleartext to encrypt (non-empty string): ")
    while len(cleartext) == 0:
        cleartext = input("The cleartext cannot be empty. Please enter the cleartext again: ")

    # Encrypt the cleartext
    encrypted = vigE(key, cleartext)
    print(f"Encrypted ciphertext: {encrypted}")

    # Decrypt the ciphertext
    decrypted = vigD(key, encrypted)
    print(f"Decrypted plaintext: {decrypted}")
