
import exit_point
from config import CMDLETS, CMDLETS_DESCRIPTION, PROMPT_SYMBOL, COLORS
import sys, os

def unknown_command(cmd):
    print(f"{COLORS["bold"]}{COLORS["red"]}{PROMPT_SYMBOL}Name \"{cmd}\" it is not recognized as a cmdlet, function, or executable program file. "
          f"\nPlease check the spelling of your command and try to enter the command again.{COLORS["reset"]}")
def stdout_func(msg):
    try:
        if msg.startswith("stdout \""):
            if msg.endswith("\""):
                msg_content = msg[8:-1]
                print(f"{PROMPT_SYMBOL}{msg_content}")
            else:
                print(f"{PROMPT_SYMBOL}{COLORS["red"]}Stdout Error{COLORS["reset"]}")
        else:
            print(f"{PROMPT_SYMBOL}Stdout Error")

    except:
        print(f"{PROMPT_SYMBOL}Invalid stdout format")
def sys_info_func(args=''):
    print(f"{PROMPT_SYMBOL}{COLORS['bold']}System information:{COLORS['reset']}")
    print(f"{PROMPT_SYMBOL}Python version: {sys.version}")
    print(f"{PROMPT_SYMBOL}OS: {os.name}")
    print(f"{PROMPT_SYMBOL}Current directory: {os.getcwd()}")

def help_func(arg=''):
    if arg == '':
        for item, desc in CMDLETS_DESCRIPTION.items():
            print(f"{PROMPT_SYMBOL}{item} -- {desc}")
    elif arg == "exit":
        print(f"{PROMPT_SYMBOL}The exit cmdlet exit from the system process")
    elif arg == "stdout":
        print(f"{PROMPT_SYMBOL}The \"stdout\" command allows you to print text to the console. "
              f"\nThe written text will be automatically interpreted into a string and stored in memory. "
              f"\nExample of writing this command: {COLORS["italic"]}{COLORS["magenta"]}stdout{COLORS["reset"]} {COLORS["italic"]}{COLORS["yellow"]}\"Hello, World!\"{COLORS["reset"]}. "
              f"\nAll the text that will be inside the quotes will be displayed on the screen and automatically interpreted as a string.")
    else:
        print(f"{PROMPT_SYMBOL}Invalid argument \"{arg}\" from function \"help\"")

def process_command(enter):
    enter = enter.strip()
    if enter == CMDLETS[1]:
        exit_point.log_out()

    elif enter == CMDLETS[0]:
        help_func("")

    elif enter.startswith(f"{CMDLETS[0]}("):
        if enter.endswith(")"):
            help_func(enter[5:-1])
        else:
            print("None valid format \"help()\" function.")
    elif enter.strip() == f"{CMDLETS[0]}":
        help_func('')

    elif enter.startswith(f"{CMDLETS[2]} "):
        stdout_func(enter)
    elif enter == CMDLETS[3]:
        sys_info_func()
    elif enter != "":
        if not str(enter).isdigit():
            unknown_command(enter)
