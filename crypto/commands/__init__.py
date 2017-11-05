from .setup import run as run_setup
from .add import run as run_add

commands = {
    'setup': run_setup,
    'add': run_add,
}