import argparse


def encrypt(message,shift):
    encrypted_message = ''

    for letter in message:
        if letter.isalpha():
            if letter.isupper():
                base = ord('A')
            else:
                base = ord('a')
        
            position = ord(letter) - base
            new_position = (position + shift) % 26
            new_letter = chr(new_position + base)

            encrypted_message += new_letter
        
        else:
            encrypted_message += letter
    return encrypted_message


def decrypt(message,shift):
    decrypted_message = ''

    for letter in message:
        if letter.isalpha():
            if letter.isupper():
                base = ord('A')
            else:
                base = ord('a')
        
            position = ord(letter) - base
            new_position = (position - shift) % 26
            new_letter = chr(new_position + base)

            decrypted_message += new_letter
        
        else:
            decrypted_message += letter
    return decrypted_message