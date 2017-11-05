from .setup import run as run_setup
from .add import run as run_add
from .export import run as run_export
from .encrypt import run as run_encrypt
from .decrypt import run as run_decrypt

commands = {
    'setup': run_setup,
    'add': run_add,
    'export': run_export,
    'encrypt': run_encrypt,
    'decrypt': run_decrypt,
}