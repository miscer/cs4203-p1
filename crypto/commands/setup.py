from typing import Optional

import peewee
from nacl.public import PrivateKey

from crypto.models import Me


def get_me(profile) -> Optional[Me]:
    try:
        return Me.get(profile=profile)
    except peewee.DoesNotExist:
        return None


def create_me(name, profile):
    private_key = PrivateKey.generate()
    return Me.create(name=name, private_key=private_key, profile=profile)


def run(args):
    me = get_me(args.profile)

    if me is None or args.force:
        Me.delete().where(Me.profile == args.profile).execute()
        me = create_me(args.name, args.profile)

        print('Hello {}!'.format(me.name))
        print('Your keys are now saved.')
    else:
        print('Crypto is already set up.')
        print('Use the --force flag to set it up again.')
        return 1
