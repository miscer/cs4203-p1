from nacl.encoding import HexEncoder
from peewee import DoesNotExist

from ..models import Me, Person


def print_key(key):
    encoded = key.encode(encoder=HexEncoder)
    print(encoded.decode('utf-8'))


def run(args):
    if args.email is None:
        try:
            me = Me.get(profile=args.profile)
        except DoesNotExist:
            print('You need to run setup first!')
            return 1

        print_key(me.private_key.public_key)
    else:
        try:
            person = Person.get(email=args.email, profile=args.profile)
        except DoesNotExist:
            print('Nobody with email {} exists.'.format(args.email))
            return 1

        print_key(person.public_key)
