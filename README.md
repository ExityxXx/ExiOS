# Exi OS - A Simple Pseudo-Operating System in Python



**Exi OS** - это учебный проект, представляющий собой простую псевдо-операционную систему, разработанную на языке Python. Она предназначена для демонстрации базовых принципов работы операционных систем, таких как обработка команд, файловая система, и взаимодействие с пользователем через командную строку.

## ✨ Key Features
-   **Interactive Command Line Interface (CLI):** A simple and intuitive command line interface for executing commands.
-   **Built-in Commands:** Support for essential commands:
    - `stdout "<text>"`: Prints the given text to the console.
    - `help` or `help(arg)`: Get list commands
    - `exit`: Finish programm
 
-   **Basic File System:** A simplified hierarchical file system for storing files and directories.
-   **Colorized Output:** Enhanced terminal output with ANSI escape codes for colorful text.
-   **Configurable:** Easily customize the OS's name, welcome message, prompt symbol, and colors through the config.py file.

## 🚀 Getting Started

### 🛠️ Prerequisites

-   Python 3.6+ (preferably 3.8 or higher)

### 📦 Installation

1.  Clone the repository:

    ```bash
    git clone https://github.com/ExityxXx/ExiOS
    ```
2.  Navigate to the project directory:

    ```bash
    cd ExiOS
    ```
3.  Run the entry_point.py script:

    ```bash
    python entry_point.py
    ```

## 💻 Usage

After starting the application, you will be presented with a welcome message and the Exi OS command prompt: `>>> `.

### ⌨️ Example
```bash
 _____          ___     ___    ____  
| ____| __  __ |_ _|   / _ \  / ___| 
|  _|   \ \/ /  | |   | | | | \___ \ 
| |___   >  <   | |   | |_| |  ___) |
|_____| /_/\_\ |___|   \___/  |____/

Welcome to Exi OS. Type ‘help’ for a list of commands.
>>> help
>>> help -- Show all cmdlets, functions and os syntax.
>>> exit -- Finish system process.
>>> stdout -- Log text
>>> help(stdout)
>>> The "stdout" command allows you to print text to the console. 
The written text will be automatically interpreted into a string and stored in memory. 
Example of writing this command: stdout "Hello, World!". 
All the text that will be inside the quotes will be displayed on the screen and automatically interpreted as a string.
>>> stdout "Hi! This is a README.md for repository"
>>> Hi! This is a README.md for repository
>>> exit
>>> Log out of the system...

