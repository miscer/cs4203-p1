import argparse

import sys

from .commands import commands

parser = argparse.ArgumentParser(prog='crypto', description='Simple encryption utility')
parser.add_argument('--profile', default='default', help='use a different profile')

subparsers = parser.add_subparsers(dest='command')

setup_parser = subparsers.add_parser('setup', description='Set up a profile')
setup_parser.add_argument('name', help='name for the profile')
setup_parser.add_argument('--force', action='store_true', help='overwrite existing profile')

add_parser = subparsers.add_parser('add', description='Add new person and their public key')
add_parser.add_argument('name', help='name of the person')
add_parser.add_argument('email', help='email of the person')
add_parser.add_argument('key', help='public key of the person')

export_parser = subparsers.add_parser('export', description='Export public keys')
export_parser.add_argument('email', nargs='?', help='email for the public key; if omitted returns your public key')

encrypt_parser = subparsers.add_parser('encrypt', description='Encrypt a message')
encrypt_parser.add_argument('email', help='recipient\'s email')
encrypt_parser.add_argument('input', nargs='?', help='input file; if omitted uses standard input')
encrypt_parser.add_argument('output', nargs='?', help='output file; if omitted uses standard output')

decrypt_parser = subparsers.add_parser('decrypt', description='Decrypt a message')
decrypt_parser.add_argument('email', help='sender\'s email')
decrypt_parser.add_argument('input', nargs='?', help='input file; if omitted uses standard input')
decrypt_parser.add_argument('output', nargs='?', help='output file; if omitted uses standard output')

list_parser = subparsers.add_parser('list', description='List all added public keys')

hash_parser = subparsers.add_parser('hash', description='Generator or check a message hash')
hash_parser.add_argument('--hasher', choices=('sha256', 'sha512', 'blake2b'), default='blake2b', help='hash function')

hash_subparsers = hash_parser.add_subparsers(dest='hash_command')

hash_generate = hash_subparsers.add_parser('generate', description='Generate a hash of a message')
hash_generate.add_argument('input', nargs='?', help='input file; if omitted uses standard input')

hash_check = hash_subparsers.add_parser('check', description='Check if the hash matches the message')
hash_check.add_argument('hash', help='hash to compare with')
hash_check.add_argument('input', nargs='?', help='input file; if omitted uses standard input')

args = parser.parse_args()

if args.command is None:
    parser.print_usage()
else:
    run_command = commands[args.command]
    run_command(args)