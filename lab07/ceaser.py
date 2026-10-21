import argparse
from cryptlib import encrypt,decrypt

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-e', '--encrypt', action='store_true', help='encrypt a message')
    parser.add_argument('-d', '--decrypt', action='store_true', help='decrypt a message')
    parser.add_argument('-m', '--message', required=True, help='your message')
    parser.add_argument('-s', '--shift', required=True, help='how much to shift characters')
    args = parser.parse_args()

    if args.encrypt and args.decrypt:
        print('Only one of -e or -d can be used at a time')
        return
    
    if args.encrypt:
        encrypted_message = encrypt(args.message, int(args.shift))
        print(encrypted_message)

    if args.decrypt:
        decrypted_message = decrypt(args.message, int(args.shift))
        print(decrypted_message)

if __name__ == '__main__':
    main()