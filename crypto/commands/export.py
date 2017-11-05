from nacl.encoding import HexEncoder
from peewee import DoesNotExist

from ..models import Me, Person


def get_me():
    return Me.get()


def get_person(email):
    return Person.get(email=email)


def print_key(key):
    encoded = key.encode(encoder=HexEncoder)
    print(encoded.decode('utf-8'))


def run(args):
    if args.email is None:
        try:
            me = get_me()
        except DoesNotExist:
            print('You need to run setup first!')
            return

        print('Your public key:')
        print_key(me.private_key.public_key)
    else:
        try:
            person = get_person(args.email)
        except DoesNotExist:
            print('Nobody with email {} exists.'.format(args.email))
            return

        print('Public key for {}:'.format(person.name))
        print_key(person.public_key)