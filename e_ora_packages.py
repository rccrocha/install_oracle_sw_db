import subprocess

def sh(command):
    subprocess.call(command, shell=True)

def ora_pkgs():
    print ('Packages script called! Installing new packages!')
    pacotes = [
           "bc",
           "binutils",
           "compat-libcap1",
           "compat-libstdc++-33",
           "elfutils-libelf",
           "elfutils-libelf-devel",
           "fontconfig-devel",
           "glibc",
           "glibc-devel",
           "ksh",
           "libaio",
           "libaio-devel",
           "libdtrace-ctf-devel",
           "libXrender",
           "libXrender-devel",
           "libX11",
           "libXau",
           "libXi",
           "libXtst",
           "libgcc",
           "librdmacm-devel",
           "libstdc++",
           "libstdc++-devel",
           "libxcb",
           "make",
           "smartmontools",
           "sysstat",
           "net-tools",
           "nfs-utils",
           "python",
           "python-configshell",
           "python-rtslib",
           "python-six",
           "targetcli",
           "https://yum.oracle.com/repo/OracleLinux/OL8/appstream/x86_64/getPackage/oracle-database-preinstall-19c-1.0-2.el8.x86_64.rpm"
          ]

    for pkgs in pacotes:
        print (f'''
Installing {pkgs} now
''')
        sh(f'yum install -y {pkgs}')
        print ('''
Done!
''')

