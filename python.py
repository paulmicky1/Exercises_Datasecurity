'''
	python.py

	Copyright (c) PAUL MICKY D COSTA
	Licensed under the MIT license: https://opensource.org/license/mit
'''
def caesarE(key, cleartext):
    """
    Encrypt the cleartext using Caesar's Cipher with the given key.
    
    Parameters:
    key (int): The number of positions to shift the alphabet.
    cleartext (str): The text to be encrypted.
    
    Returns:
    str: The encrypted ciphertext.
    """
    ciphertext = ""
    
    for char in cleartext:
        if char.isalpha():
            # Handle uppercase letters
            if char.isupper():
                ciphertext += chr((ord(char) + key - 65) % 26 + 65)
            # Handle lowercase letters
            else:
                ciphertext += chr((ord(char) + key - 97) % 26 + 97)
        else:
            # Keep non-alphabetic characters unchanged
            ciphertext += char
            
    return ciphertext


def caesarD(key, ciphertext):
    """
    Decrypt the ciphertext using Caesar's Cipher with the given key.
    
    Parameters:
    key (int): The number of positions to shift the alphabet.
    ciphertext (str): The text to be decrypted.
    
    Returns:
    str: The decrypted plaintext.
    """
    plaintext = ""
    
    for char in ciphertext:
        if char.isalpha():
            # Handle uppercase letters
            if char.isupper():
                plaintext += chr((ord(char) - key - 65) % 26 + 65)
            # Handle lowercase letters
            else:
                plaintext += chr((ord(char) - key - 97) % 26 + 97)
        else:
            # Keep non-alphabetic characters unchanged
            plaintext += char
            
    return plaintext


# Main program to interact with the user
if __name__ == "__main__":
    # Take user input for the key (ensuring it's a positive integer)
    while True:
        try:
            key = int(input("Enter the Caesar Cipher key (positive integer): "))
            if key <= 0:
                print("The key must be a positive integer. Try again.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    # Take user input for the cleartext (to be encrypted)
    cleartext = input("Enter the cleartext to encrypt: ")

    # Encrypt the cleartext
    encrypted = caesarE(key, cleartext)
    print(f"Encrypted ciphertext: {encrypted}")

    # Decrypt the ciphertext
    decrypted = caesarD(key, encrypted)
    print(f"Decrypted plaintext: {decrypted}")
