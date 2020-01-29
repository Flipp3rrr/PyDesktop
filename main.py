print("?> Booting PythonOS...")
print("?> Starting modules...")
import tkinter as tk
import sys
print("> Modules started!")
print("> PythonOS booted succesfully!")
print("> Looking for desktop environment...")
print("> No desktop environment found!")
print("> Booting to shell...")
print("> Shell ready!")
print()
print("Welcome to PythonOS!")

while True:
    cmd = input("BasicSHELL> ")
    
    if cmd == "exit":
        sys.exit()