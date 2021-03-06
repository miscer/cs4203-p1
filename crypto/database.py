import os
import peewee
import nacl.public, nacl.encoding


db_file = os.environ.get('DATABASE', 'crypto.db')
database = peewee.SqliteDatabase(db_file)


class BaseModel(peewee.Model):
    class Meta:
        database = database


class PublicKeyField(peewee.CharField):
    def db_value(self, value: nacl.public.PublicKey):
        return value.encode(encoder=nacl.encoding.HexEncoder)

    def python_value(self, value):
        return nacl.public.PublicKey(value, encoder=nacl.encoding.HexEncoder)


class PrivateKeyField(peewee.CharField):
    def db_value(self, value: nacl.public.PrivateKey):
        return value.encode(encoder=nacl.encoding.HexEncoder)

    def python_value(self, value):
        return nacl.public.PrivateKey(value, encoder=nacl.encoding.HexEncoder)
