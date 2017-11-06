import sys

import nacl.hash, nacl.encoding


def run(args):
    if args.hash_command == 'generate':
        input_file = open(args.input, 'rb') if args.input else sys.stdin.buffer
        message = input_file.read()

        digest = nacl.hash.blake2b(message, encoder=nacl.encoding.HexEncoder)
        print(digest.decode('utf-8'))
