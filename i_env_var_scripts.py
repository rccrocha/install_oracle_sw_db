import subprocess

def sh(command):
    subprocess.call(command, shell=True)

def env_var():

    print (f"""
    __________________________________________________
    |                                                 |
    | Creating the set Environmental Variables script |
    |_________________________________________________|
    """)

    set_env = f'''#Oracle Settings

export DB_VERSION=$1
export DBNAME=$2

export TMP=/tmp
export TMPDIR=$TMP

export ORACLE_HOSTNAME=ol8-prod
export ORACLE_UNQNAME=$DBNAME
export ORACLE_BASE=/oracle/$DB_VERSION
export ORACLE_HOME=$ORACLE_BASE/oh
export ORA_INVENTORY=$ORACLE_BASE/oraInventory
export ORACLE_SID=$ORACLE_UNQNAME
export DATA_DIR=/oradata
export TNS_ADMIN=$ORACLE_HOME/network/admin

export PATH=/usr/sbin:/usr/local/bin:$PATH
export PATH=$ORACLE_HOME/bin:$PATH:$ORACLE_HOME/OPatch

export LD_LIBRARY_PATH=$ORACLE_HOME/lib:/lib:/usr/lib
export CLASSPATH=$ORACLE_HOME/jlib:$ORACLE_HOME/rdbms/jlib

alias oraenv='. $USER/scripts/setEnv.ksh'
alias p='python3'
alias pmon='ps -ef | grep pmon'
alias sysdba='sqlplus / as sysdba'
'''

    with open('/home/oracle/scripts/setEnv.sh', 'w') as se:
        se.write(set_env)
        se.close()

    sh('echo ". /home/oracle/scripts/setEnv.sh" >> /home/oracle/.bash_profile')

    print (f"""
__________________________________________
|                                         |
| Creating start and stop database script |
|_________________________________________|
""")

    sh('''cat > /home/oracle/scripts/start_all.sh <<EOF
#!/bin/bash
. /home/oracle/scripts/setEnv.sh

export ORAENV_ASK=NO
. oraenv
export ORAENV_ASK=YES

dbstart \$ORACLE_HOME
EOF

cat > /home/oracle/scripts/stop_all.sh <<EOF
#!/bin/bash
. /home/oracle/scripts/setEnv.sh

export ORAENV_ASK=NO
. oraenv
export ORAENV_ASK=YES

dbshut \$ORACLE_HOME
EOF''')

    sh('''cp g_oracle_user_server_install.py /home/oracle/scripts/g_oracle_user_server_install.py
cp h_db_creation.py /home/oracle/scripts/h_db_creation.py
chown -R oracle:oinstall /home/oracle/scripts
chmod u+x /home/oracle/scripts/*''')
