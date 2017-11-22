import sys
from nacl.public import Box
from peewee import DoesNotExist

from ..models import Me, Person


def run(args):
    try:
        me = Me.get(profile=args.profile)
    except DoesNotExist:
        print('You need to run setup first!')
        return 1

    try:
        recipient = Person.get(email=args.email, profile=args.profile)
    except DoesNotExist:
        print('Nobody with email {} exists.'.format(args.email))
        return 1

    private_key = me.private_key
    public_key = recipient.public_key

    try:
        input_file = open(args.input, 'rb') if args.input else sys.stdin.buffer
    except FileNotFoundError:
        print('File does not exist')
        return 1
    
    output_file = open(args.output, 'wb') if args.output else sys.stdout.buffer

    box = Box(private_key, public_key)
    encrypted_message = box.encrypt(input_file.read())
    output_file.write(encrypted_message)
