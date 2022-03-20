import subprocess
import sys

def sh(command):
     subprocess.call(command, shell=True)

db_name   = sys.argv[1]
pswd      = sys.argv[2]
dbversion = sys.argv[3] 
host      = 'ol8-prod'

print (f'''
DB Version: {dbversion}
Password  : {pswd}
DB Name   : {db_name}

I'm running as''')
sh('whoami')

if dbversion == '21':
    sh(f'''. /home/oracle/scripts/setEnv.sh {dbversion} {db_name}
cd $ORACLE_HOME
dbca -silent -createDatabase                                                   \
     -templateName General_Purpose.dbc                                         \
     -gdbname {db_name}.{host} -sid {db_name} -responseFile NO_VALUE           \
     -characterSet AL32UTF8                                                    \
     -sysPassword {pswd}                                                       \
     -systemPassword {pswd}                                                    \
     -createAsContainerDatabase true                                           \
     -numberOfPDBs 1                                                           \
     -pdbName pdb{db_name}                                                     \
     -pdbAdminPassword pdb{pswd}                                               \
     -databaseType MULTIPURPOSE                                                \
     -memoryMgmtType auto_sga                                                  \
     -totalMemory 2000                                                         \
     -storageType FS                                                           \
     -datafileDestination "/oradata/"	                                       \
     -redoLogFileSize 50                                                       \
     -emConfiguration NONE                                                     \
     -ignorePreReqs
''')
else:
    sh(f'''. /home/oracle/scripts/setEnv.sh {dbversion} {db_name}
cd $ORACLE_HOME
dbca -silent -createDatabase                                              \
     -templateName General_Purpose.dbc                                    \
     -gdbname {db_name}.{host} -sid {db_name} -responseFile NO_VALUE      \
     -characterSet AL32UTF8                                               \
     -sysPassword {pswd}                                                  \
     -createAsContainerDatabase false                                     \
     -systemPassword {pswd}                                               \
     -databaseType MULTIPURPOSE                                           \
     -totalMemory 2000                                                    \
     -memoryMgmtType auto_sga                                             \
     -storageType FS                                                      \
     -datafileDestination "/oradata/"	                                  \
     -redoLogFileSize 50                                                  \
     -emConfiguration NONE                                                \
     -ignorePreReqs
''')

