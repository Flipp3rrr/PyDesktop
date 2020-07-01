print("BOOT> boot(PythonOS)")
print()
print("Booting PythonOS...")

print("Importing modules...")
try:
    import tkinter as tk
    import sys
    import time
    print("Imported modules succesfully!")
except Exception as error: 
    print('ERR$', error) 

print("PythonOS booted succesfully!")
print("Looking for desktop environment...")
print("No desktop environment found!")
print("Booting to shell...")
print("Shell ready!")
print()
print("WARN$ Files are not encrypted!")
print()
print("Welcome to PythonOS!")

while True:
    cmd = input("BasicSHELL> ")
    
    if cmd == "help":
        print("Basic commands:\n  help: display help text\n  exit: stop PythonOS\n  ls: Show directory contents\n  cd: Go to direcotry")

    if cmd == "shutdown":
        print("Shutting down...")
        sys.exit()

    if cmd == "ls":
        # TO DO!!!
        print("The current directory contains the following:\nEMPTY")
    
    if cmd == "cd":
        # TO DO!!!
        print("...")
