from .setup import run as run_setup
from .add import run as run_add
from .export import run as run_export
from .encrypt import run as run_encrypt
from .decrypt import run as run_decrypt
from .list import run as run_list
from .hash import run as run_hash

commands = {
    'setup': run_setup,
    'add': run_add,
    'export': run_export,
    'encrypt': run_encrypt,
    'decrypt': run_decrypt,
    'list': run_list,
    'hash': run_hash,
}