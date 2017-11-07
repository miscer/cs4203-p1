from humanfriendly.tables import format_smart_table
from nacl.encoding import HexEncoder

from crypto.models import Person


def encode_key(key):
    encoded = key.encode(encoder=HexEncoder)
    return encoded.decode('utf-8')


def run(args):
    people = Person.select().where(Person.profile == args.profile)
    rows = [(person.name, person.email, encode_key(person.public_key)) for person in people]
    table = format_smart_table(rows, ('Name', 'Email', 'Public Key'))
    print(table)