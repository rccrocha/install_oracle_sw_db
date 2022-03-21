from c_clean_full_install import cleanfullinstall
from datetime             import datetime
from ca_del_user          import deluser
from f_ora_users          import orausers
from d_sys_check          import syscheck
from b_full_install       import fullinstall

import os
import psutil
import pwd
import subprocess
import sys
import time

help = '''
______________________________________________________________________
|                                                                     |
| USAGE                                                               |
|_____________________________________________________________________|

Silent install of Oracle binaries and creation of a database.

Usage: install_db_server.py <database> <sys_password>
'''

def sh(command):
    subprocess.call(command, shell=True)

start = datetime.now()

try:
    dbname = sys.argv[1]
    syspwd = sys.argv[2]
except:
    print (help)
    exit()

install = input('''
______________________________________________________________________
|                                                                     |
| What do you want to do:                                             |
|                                                                     |
| 1 -> Install Oracle Database Software and Create a new database     |
| 2 -> Create only a new empty database                               |
| 3 -> Clean everything and install Oracle DB Server and empty db     |
|_____________________________________________________________________|

''')

if int(install) == 1:
    print ('''
______________________________________________________________________
|                                                                     |
| New Installation of Oracle Database Server and new empty database   |
|_____________________________________________________________________|
''')

    version = input('''
______________________________________________________________________
|                                                                     |
| What version do you want to install ?                               |
|                                                                     |
| 1 -> 11							      |
| 2 -> 12cR1 							      |
| 3 -> 12cR2                                                          |
| 4 -> 19c                                                            |
| 5 -> 21c                                                            |
|_____________________________________________________________________|

''')

    if int(version) == 1:
        fullinstall(dbname,"11","112040.zip",syspwd)
    elif int(version) == 2:
        fullinstall(dbname,"121","121002.zip",syspwd)
    elif int(version) == 3:
        fullinstall(dbname,"122","122010.zip",syspwd)

    elif int(version) == 4:
        fullinstall(dbname,"19","193000.zip",syspwd)
    else:
        fullinstall(dbname,"21","213000.zip",syspwd)

elif int(install) == 2:
    print ('''
______________________________________________________________________
|                                                                     |
| Creating new empty database                                         |
|_____________________________________________________________________|
''')


    version = input('''
______________________________________________________________________
|                                                                     |
| In what version do you want to create the database ?                |
|                                                                     |
| 1 -> 11                                                             |
| 2 -> 12cR1                                                          |
| 3 -> 12cR2							      |
| 4 -> 19c                                                            |
| 5 -> 21c                                                            |
|_____________________________________________________________________|

''')

    if int(version) == 1:
        sh(f'su - oracle -c "python3 /home/oracle/scripts/h_db_creation.py {dbname} {syspwd} 11"')
    elif int(version) == 2:
        sh(f'su - oracle -c "python3 /home/oracle/scripts/h_db_creation.py {dbname} {syspwd} 121"')
    elif int(version) == 3:
        sh(f'su - oracle -c "python3 /home/oracle/scripts/h_db_creation.py {dbname} {syspwd} 122"')
    elif int(version) == 4:
        sh(f'su - oracle -c "python3 /home/oracle/scripts/h_db_creation.py {dbname} {syspwd} 19"')
    else:
        sh(f'su - oracle -c "python3 /home/oracle/scripts/h_db_creation.py {dbname} {syspwd} 21"')

else:
    print ('''
______________________________________________________________________
|                                                                     |
| Cleanning everything and reinstalling all                           |
|_____________________________________________________________________|
''')

    version = input('''
______________________________________________________________________
|                                                                     |
| In what version do you want to create the database ?                |
|                                                                     |
| 1 -> 11                                                             |
| 2 -> 12cR1                                                          |
| 3 -> 12cR2                                                          |
| 4 -> 19c                                                            |
| 5 -> 21c                                                            |
|_____________________________________________________________________|

''')

    if int(version) == 1:
        cleanfullinstall(dbname,"11","112040.zip",syspwd)
    elif int(version) == 2:
        cleanfullinstall(dbname,"121","121002.zip",syspwd)
    elif int(version) == 2:
        cleanfullinstall(dbname,"122","122010.zip",syspwd)
    elif int(version) == 2:
        cleanfullinstall(dbname,"19","193000.zip",syspwd)
    else:
        cleanfullinstall(dbname,"21","213000.zip",syspwd)

end = datetime.now()
elapsed = end - start
print (f'Elapsed time: {str(elapsed)[0:7]}.')

