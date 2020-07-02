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
""")

# import modules which are needed later
# - time
# - sys
# - os
# - platform
try:
    import time
    import sys
    import os
    import platform

except Exception as error: 
    print("ERR$ Fatal error while importing modules:\n     %s" % (error))
    exit()

# system information
print("--- System information ---")
plfOS = platform.system()
plfCPUarchitecture = platform.machine()
plfProcessor = platform.processor()

print("""
System   : %s
CPU arch.: %s
Processor: %s""" % (plfOS, plfCPUarchitecture, plfProcessor))
print()

# check compatibility
if plfOS != "Darwin":
    print("""
    WARNING! YOUR CURRENT OPERATING SYSTEM IS NOT SUPPORTED, PLEASE PROCEED WITH CAUTION!
    """)

# save current running directory path to var
programPath = os.path.dirname(os.path.realpath(__file__))

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

# login screen, asks for user and password
deviceUsers = fileReader("read", "/system/user.usr")
print("Choose a user:\n%s" % (deviceUsers))

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
        sys.exit("Goodbye!")

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
