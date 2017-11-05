from .setup import run as run_setup
from .add import run as run_add
from .export import run as run_export

commands = {
    'setup': run_setup,
    'add': run_add,
    'export': run_export,
}