import subprocess
import sys


def sh(command):
    subprocess.call(command,shell=True)

dbversion = sys.argv[1]
binaries  = sys.argv[2]
db_name   = sys.argv[3]

print (f'''
DB Version: {dbversion}
Binaries  : {binaries}
DB Name   : {db_name}

I'm running as''')

sh('whoami')

if dbversion != '19':
    sh(f'''. /home/oracle/scripts/setEnv.sh {dbversion} {db_name}
cd $ORACLE_HOME
echo "Unzipping the binaries {binaries}"
unzip -oq /orabkp/binaries/{binaries} -d $ORACLE_HOME
echo "Unzipping done!"
export CV_ASSUME_DISTID=OEL7.8
echo "
Starting the installer...
"
./runInstaller -ignoreSysPrereqs -ignorePrereq -waitforcompletion -showProgress -silent \
    -responseFile $ORACLE_HOME/response/db_install.rsp \
    oracle.install.option=INSTALL_DB_SWONLY \
    ORACLE_HOSTNAME=${ORACLE_HOSTNAME} \
    UNIX_GROUP_NAME=oinstall \
    INVENTORY_LOCATION=$ORA_INVENTORY \
    SELECTED_LANGUAGES=en,en_GB \
    ORACLE_HOME=$ORACLE_HOME \
    ORACLE_BASE=$ORACLE_BASE \
    oracle.install.db.InstallEdition=EE \
    oracle.install.db.OSDBA_GROUP=dba \
    oracle.install.db.OSBACKUPDBA_GROUP=dba \
    oracle.install.db.OSDGDBA_GROUP=dba \
    oracle.install.db.OSKMDBA_GROUP=dba \
    oracle.install.db.OSRACDBA_GROUP=dba \
    SECURITY_UPDATES_VIA_MYORACLESUPPORT=false \
    DECLINE_SECURITY_UPDATES=true
''')
else:
    sh(f'''. /home/oracle/scripts/setEnv.sh {dbversion} {db_name}
cd $ORACLE_HOME
echo "Unzipping the binaries {binaries}"
unzip -oq /orabkp/binaries/{binaries} -d $ORACLE_HOME
echo "Unzipping done!"
export CV_ASSUME_DISTID=OEL7.8
echo "
Starting the installer...
"
./runInstaller -ignorePrereq -waitforcompletion -silent                        \
    -responseFile $ORACLE_HOME/install/response/db_install.rsp                 \
    oracle.install.option=INSTALL_DB_SWONLY                                    \
    ORACLE_HOSTNAME=$ORACLE_HOSTNAME                                           \
    UNIX_GROUP_NAME=oinstall                                                   \
    INVENTORY_LOCATION=$ORA_INVENTORY                                          \
    SELECTED_LANGUAGES=en,en_GB                                                \
    ORACLE_HOME=$ORACLE_HOME	                                               \
    ORACLE_BASE=$ORACLE_BASE                                                   \
    oracle.install.db.InstallEdition=EE                                        \
    oracle.install.db.OSDBA_GROUP=dba                                          \
    oracle.install.db.OSBACKUPDBA_GROUP=dba                                    \
    oracle.install.db.OSDGDBA_GROUP=dba                                        \
    oracle.install.db.OSKMDBA_GROUP=dba                                        \
    oracle.install.db.OSRACDBA_GROUP=dba                                       \
    SECURITY_UPDATES_VIA_MYORACLESUPPORT=false                                 \
    DECLINE_SECURITY_UPDATES=true

echo "
###################
# Server installed!
###################
"
_______________________________
|                              |
| Installing Listener          |
|______________________________|

netca -silent -responseFile $ORACLE_HOME/assistants/netca/netca.rsp
''')
