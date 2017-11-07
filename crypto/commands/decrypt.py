import sys
from nacl.public import Box
from peewee import DoesNotExist

from ..models import Me, Person


def run(args):
    try:
        me = Me.get(profile=args.profile)
    except DoesNotExist:
        print('You need to run setup first!')
        return

    try:
        recipient = Person.get(email=args.email, profile=args.profile)
    except DoesNotExist:
        print('Nobody with email {} exists.'.format(args.email))
        return

    private_key = me.private_key
    public_key = recipient.public_key

    input_file = open(args.input, 'rb') if args.input else sys.stdin.buffer
    output_file = open(args.output, 'wb') if args.output else sys.stdout.buffer

    box = Box(private_key, public_key)
    decrypted_message = box.decrypt(input_file.read())
    output_file.write(decrypted_message)
