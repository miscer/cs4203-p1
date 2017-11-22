from nacl.encoding import HexEncoder
from nacl.public import PublicKey

from crypto.models import Person


def create_person(name, email, public_key, profile):
    return Person.create(name=name, email=email, public_key=public_key, profile=profile)


def run(args):
    try:
        public_key = PublicKey(args.key, HexEncoder)
    except:
        print('The key is not valid.')
        return 1

    person = create_person(args.name, args.email, public_key, args.profile)
    print('Added {}!'.format(person.name))
