print("""
Welcome to

  _____            _____                         _       _
 / ___ \          |  __ \                       | |   __| |__
| |   | |         | |  \ \                      | |  |__   __|
| |   | |         | |   \ \    ______   _______ | |  __ | |       ______     _____
| |___| | _    _  | |    | |  /  ___/  /  ____/ | | / / | |      /  __  \   / ___ \ 
|  ____/ | |  | | | |    | | | |_____  \____ \  | |/ /  | |     |  /  \  | | |   | |
| |      | |  | | | |   / /  |  ____/       \ \ |   <   | |     | |    | | | |   | |
| |      | |__| | | |__/ /   | |_____  _____/ / | |\ \  | |____ |  \__/  | | |___| |
|_|       \___  | |_____/     \_____/  \_____/  |_| \_\ \_____/  \______/  |  ____/
         _____| |                                                          | |
         \______/                                                          |_|

The free and open-source cross-platform desktop environment written in Python.

===
""")

# import modules which are needed later
# - time
# - sys
# - os
# - platform
print("Importing modules...")
try:
    import time
    import sys
    import os
    import platform
    print("Modules imported succesfully!")

except Exception as error: 
    print("ERR$ Failed to import modules, more information:\n", error, "\n")
    quit()

# system information
print()
print("Checking system information...")
plfOS = platform.system()
plfCPUarchitecture = platform.machine()
plfProcessor = platform.processor()

print("""
System   : %s
CPU arch.: %s
Processor: %s""" % (plfOS, plfCPUarchitecture, plfProcessor))
print()

# save current running directory path to var
programPath = os.path.dirname(os.path.realpath(__file__))
print("Current dir.: ", programPath)

# random gibberish that looks cool
print("""PyDesktop started succesfully!
Starting shell...
Shell ready!
Setting up system defs...""")

# file reading
def fileReader(fileAct, filePath):
    try:
        # check os
        if plfOS == "Darwin":
            # check action
            if fileAct == "read":
                # read file
                filePath1 = programPath + filePath
                fileC = open(filePath1)
                fileC1 = fileC.read()
                # return file contents
                return fileC1
    except Exception as error:
        sys.exit("ERR$ Fatal error while reading files:\n     %s" % (error)) 

print("Finished setting up defs!")
print("Welcome to PyDesktop")
print()

# login screen, asks for user and password


# basic shell, maybe this shouldn't be here but it is for now
while True:
    cmd = input("SHELL> ")
    
    if cmd == "help":
        print("""
        Basic commands:
            help: display help text
            exit: stop PythonOS
            ls: Show directory contents
            cd: Go to direcotry
        """)
    if cmd == "exit":
        sys.exit()

    if cmd == "shutdown":
        # TO DO!!
        print("FEATURE IS //TBD//")
        sys.exit()

    if cmd == "ls":
        # TO DO!!
        print("FEATURE IS //TBD//")
    
    if cmd == "cd":
        # TO DO!!
        print("FEATURE IS //TBD//")
