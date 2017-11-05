from typing import Optional

import peewee
from nacl.public import PrivateKey

from crypto.models import Me


def get_me() -> Optional[Me]:
    try:
        return Me.get()
    except peewee.DoesNotExist:
        return None


def create_me(name):
    private_key = PrivateKey.generate()
    return Me.create(name=name, private_key=private_key)


def run(args):
    me = get_me()

    if me is None or args.force:
        Me.delete().execute()
        me = create_me(args.name)

        print('Hello {}!'.format(me.name))
        print('Your keys are now saved.')
    else:
        print('Crypto is already set up.')
        print('Use the --force flag to set it up again.')

