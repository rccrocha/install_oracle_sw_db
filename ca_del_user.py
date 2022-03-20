import subprocess

def sh(command):
    subprocess.call(command, shell=True)

def deluser():
    sh(f'''userdel -rf oracle
groupdel -f oinstall
groupdel -f dba
groupdel -f oper
groupdel -f backupdba
groupdel -f dgdba
groupdel -f kmdba
groupdel -f asmdba
groupdel -f asmoper
groupdel -f asmadmin
groupdel -f racdba
rm -rf /home/oracle /u01 /u02 /etc/oratab /oracle/* /oradata/*''')

