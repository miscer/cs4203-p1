import argparse

import sys

from .commands import commands

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(dest='command')

setup_parser = subparsers.add_parser('setup')
setup_parser.add_argument('name')
setup_parser.add_argument('--force', action='store_true')

add_parser = subparsers.add_parser('add')
add_parser.add_argument('name')
add_parser.add_argument('email')
add_parser.add_argument('key')

export_parser = subparsers.add_parser('export')
export_parser.add_argument('email', nargs='?')

encrypt_parser = subparsers.add_parser('encrypt')
encrypt_parser.add_argument('email')
encrypt_parser.add_argument('input', nargs='?')
encrypt_parser.add_argument('output', nargs='?')

decrypt_parser = subparsers.add_parser('decrypt')
decrypt_parser.add_argument('email')
decrypt_parser.add_argument('input', nargs='?')
decrypt_parser.add_argument('output', nargs='?')

list_parser = subparsers.add_parser('list')

hash_parser = subparsers.add_parser('hash')
hash_subparsers = hash_parser.add_subparsers(dest='hash_command')

hash_generate = hash_subparsers.add_parser('generate')
hash_generate.add_argument('input', nargs='?')

hash_check = hash_subparsers.add_parser('check')
hash_check.add_argument('hash')
hash_check.add_argument('input', nargs='?')

args = parser.parse_args()

if args.command is None:
    parser.print_usage()
else:
    run_command = commands[args.command]
    run_command(args)