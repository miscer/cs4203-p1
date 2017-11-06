import sys

import nacl.hash, nacl.encoding


def generate_file_hash(input):
    return nacl.hash.blake2b(input.read(), encoder=nacl.encoding.HexEncoder)


def run(args):
    if args.hash_command == 'generate':
        input_file = open(args.input, 'rb') if args.input else sys.stdin.buffer
        file_hash = generate_file_hash(input_file)
        print(file_hash.decode('utf-8'))

    elif args.hash_command == 'check':
        input_file = open(args.input, 'rb') if args.input else sys.stdin.buffer
        file_hash = generate_file_hash(input_file)

        if file_hash.decode('utf-8') == args.hash:
            print('All good!')
        else:
            print('Watch out, something is fishy here!')

