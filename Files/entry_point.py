import pyfiglet as pyfig
from command_recognizer import process_command
import config

def main():
    pyfig.print_figlet(f"E x I  O S")
    print(config.WELCOME_MESSAGE)
    while True:
        command = input(config.PROMPT_SYMBOL)
        process_command(command)


if __name__ == '__main__':
    main()
