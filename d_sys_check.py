from termcolor import colored

import os
import psutil
import subprocess

def sh(command):
    subprocess.call(command, shell=True)

def syscheck(binaries):
    print (f'''
________________
|               |
| SYSTEM CHECKS |
|_______________|

1st - Binaries files -> {binaries}
----------------------------------
''')

    for file in os.listdir('/orabkp/binaries/'):
        if binaries != file:
            print (f"""File exists! {colored('Passed', 'green')}
""")
            break
        else:
            break

    print ('''
2nd - Disk space
----------------
''')

    dskspc = os.statvfs("/oracle")
    disk   = round(((dskspc.f_frsize * dskspc.f_bavail)/1024/1024/1024),2)

    if disk < 10:
        print (f"""Requirement  Minimum  Available  Status
-----------  -------  ---------  ------
Disk Space   10 G     {disk}G{'':>6}{colored('Failed', 'red')}
""")
        exit()
    else:
        print (f"""Requirement  Minimum  Available  Status
-----------  -------  ---------  ------
Disk Space   10 G     {disk}G{'':>6}{colored('Passed', 'green')}
""")

    print ('''
3rd - Memory RAM
----------------
''')

    mem = round((psutil.virtual_memory().total)/1024.**3,2)

    if mem < 2:
        print (f"""Requirement  Minimum  Available  Status
-----------  -------  ---------  ------
Memory RAM   2 G      {mem}G{'':>6}{colored('Failed', 'red')}
""")
        exit()
    else:
        print (f"""Requirement  Minimum  Available  Status
-----------  -------  ---------  ------
Memory RAM   2 G      {mem}G{'':>6}{colored('Passed', 'green')}
""")

    print ("""###########################
### System checks done! ###
###########################""")
