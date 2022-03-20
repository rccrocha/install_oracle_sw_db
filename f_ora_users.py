import subprocess

def sh(command):
    subprocess.call(command, shell=True)

def orausers():
    sh("""groupadd -g 54321 oinstall
groupadd -g 54322 dba
groupadd -g 54323 oper
useradd -u 54321 -g oinstall -G dba,oper oracle
passwd oracle
SELINUX=permissive
setenforce Permissive
systemctl stop firewalld
systemctl disable firewalld
mkdir -p /oracle/11/oh
mkdir -p /oracle/122/oh
mkdir -p /oracle/121/oh
mkdir -p /oracle/19/oh
mkdir -p /oracle/21/oh
chown -R oracle:oinstall /oracle /oradata
chmod -R 775 /oracle /oradata
mkdir /home/oracle/scripts""")

