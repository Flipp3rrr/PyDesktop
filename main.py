print("BOOT> boot(PythonOS)")
print()
print("Booting PythonOS...")
print("Starting modules...")
import tkinter as tk
import sys
import time
print("Modules started!")
print("PythonOS booted succesfully!")
print("Looking for desktop environment...")
print("No desktop environment found!")
print("Booting to shell...")
print("Shell ready!")
print()
print("WARN$ Files are not encrypted!")
print("WARN$ No users detected!")
print("ERR $ No default user!")
print("WARN$ Logging in fallback_usr...")
print()
print("Welcome to PythonOS!")

while True:
    cmd = input("BasicSHELL> ")
    
    if cmd == "help":
        print("Basic commands:\n  help: display help text\n  exit: stop PythonOS\n  fileXPLR: File explorer")

    if cmd == "shutdown":
        print("Shutting down...")
        sys.exit()

    if cmd == "ls":
        print("The current directory contains the following:\nEMPTY")

    else:
        print("ERR_1:", cmd, "is not a valid command!")