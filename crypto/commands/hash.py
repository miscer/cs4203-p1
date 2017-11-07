import sys

import nacl.hash, nacl.encoding


def generate_file_hash(input_file, hasher):
    return hasher(input_file.read(), encoder=nacl.encoding.HexEncoder)


hashers = {
    'sha256': nacl.hash.sha256,
    'sha512': nacl.hash.sha512,
    'blake2b': nacl.hash.blake2b,
}


def run(args):
    hasher = hashers[args.hasher]

    if args.hash_command == 'generate':
        input_file = open(args.input, 'rb') if args.input else sys.stdin.buffer
        file_hash = generate_file_hash(input_file, hasher)
        print(file_hash.decode('utf-8'))

    elif args.hash_command == 'check':
        input_file = open(args.input, 'rb') if args.input else sys.stdin.buffer
        file_hash = generate_file_hash(input_file, hasher)

        if file_hash.decode('utf-8') == args.hash:
            print('All good!')
        else:
            print('Watch out, something is fishy here!')

