from d_sys_check       import syscheck
from e_ora_packages    import ora_pkgs
from f_ora_users       import orausers
from i_env_var_scripts import env_var

import os
import psutil
import pwd
import subprocess
import sys
import time

def sh(command):
    subprocess.call(command, shell=True)

def fullinstall(dbname,db_version,binaries,syspwd):

    syscheck(binaries)

    print (f"""
_______________________________
|                              |
| Installing required packaged |
|______________________________|
""")

    pkgs = input('Are the required packages installed? Enter y or n: ')

    if pkgs == 'n':
        ora_pkgs()
    else:
        print ('Packages already installed! Proceeding with the installation!')

    print (f"""
__________________________________
|                                 |
| Creating Oracle user and groups |
|_________________________________|
""")
    orausers()

    env_var()

    print (f"""
_______________________________
|                              |
| End of script with root user |
|______________________________|

####################################
___________________________________
|                                  |
| Starting script with oracle user |
|__________________________________|
""")

    sh(f'su - oracle -c "python3 /home/oracle/scripts/g_oracle_user_server_install.py {db_version} {binaries} {dbname}"')
    print ('''Starting root script installation
''')
    sh(f'/oracle/{db_version}/oh/root.sh')
    print ('''Script executed!
''')
    sh(f'su - oracle -c "python3 /home/oracle/scripts/h_db_creation.py {dbname} {syspwd} {db_version}"')
