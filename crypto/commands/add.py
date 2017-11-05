from nacl.encoding import HexEncoder
from nacl.public import PublicKey

from crypto.models import Person


def create_person(name, email, public_key):
    return Person.create(name=name, email=email, public_key=public_key)


def run(args):
    try:
        public_key = PublicKey(args.key, HexEncoder)
    except:
        print('The key is not valid.')
        return

    person = create_person(args.name, args.email, public_key)
    print('Added {}!'.format(person.name))
