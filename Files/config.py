

PROMPT_SYMBOL = ">>> "
OS_NAME = "Exi OS"
WELCOME_MESSAGE = f"""Welcome to {OS_NAME}. Type ‘help’ for a list of commands."""

CMDLETS = (
    "help",
    "exit",
    "stdout",
    "sys info"
)

CMDLETS_DESCRIPTION = {
    "help": "Show all cmdlets, functions and os syntax.",
    "exit": "Finish system process.",
    "stdout": "Log text"
}

COLORS = {
    'reset': '\033[0m',
    'red': '\033[91m',
    'green': '\033[92m',
    'yellow': '\033[93m',
    'blue': '\033[94m',
    'magenta': '\033[95m',
    'cyan': '\033[96m',
    'white': '\033[97m',
    'black': '\033[90m',
    'bg_red': '\033[41m',
    'bg_green': '\033[42m',
    'bg_yellow': '\033[43m',
    'bg_blue': '\033[44m',
    'bg_magenta': '\033[45m',
    'bg_cyan': '\033[46m',
    'bg_white': '\033[47m',
    'bg_black': '\033[40m',
    'bold': '\033[1m',
    'dim': '\033[2m',
    'italic': '\033[3m',
    'underline': '\033[4m',
    'blink': '\033[5m',
    'invert': '\033[7m'
}

