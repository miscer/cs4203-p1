import peewee
from .database import BaseModel, PublicKeyField, PrivateKeyField, database


class Person(BaseModel):
    name = peewee.CharField()
    email = peewee.CharField(unique=True)
    public_key = PublicKeyField()
    profile = peewee.CharField()


class Me(BaseModel):
    name = peewee.CharField()
    private_key = PrivateKeyField()
    profile = peewee.CharField(unique=True)


database.create_tables([Person, Me], safe=True)
