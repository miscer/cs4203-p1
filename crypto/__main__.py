import argparse
from crypto.commands import commands

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(dest='command')

setup_parser = subparsers.add_parser('setup')
setup_parser.add_argument('name')
setup_parser.add_argument('--force', action='store_true')

encrypt_parser = subparsers.add_parser('encrypt')

decrypt_parser = subparsers.add_parser('decrypt')

args = parser.parse_args()

if args.command is None:
    parser.print_usage()
else:
    run_command = commands[args.command]
    run_command(args)