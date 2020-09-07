# -*- coding: utf-8 -*-
import subprocess
import os
import socket
socket.gethostbyname(socket.gethostname())
import platform
import socket
import getpass
from datetime import datetime
now = datetime.now()
import webbrowser
import urllib
from datetime import date
print '\033[1;36m'+'''
██╗███╗   ██╗███████╗ ██████╗     ███╗   ███╗ █████╗  ██████╗██╗  ██╗██╗███╗   ██╗███████╗
██║████╗  ██║██╔════╝██╔═══██╗    ████╗ ████║██╔══██╗██╔════╝██║  ██║██║████╗  ██║██╔════╝
██║██╔██╗ ██║█████╗  ██║   ██║    ██╔████╔██║███████║██║     ███████║██║██╔██╗ ██║█████╗  
██║██║╚██╗██║██╔══╝  ██║   ██║    ██║╚██╔╝██║██╔══██║██║     ██╔══██║██║██║╚██╗██║██╔══╝  
██║██║ ╚████║██║     ╚██████╔╝    ██║ ╚═╝ ██║██║  ██║╚██████╗██║  ██║██║██║ ╚████║███████╗
╚═╝╚═╝  ╚═══╝╚═╝      ╚═════╝     ╚═╝     ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝╚══════╝
                                                                                          

'''+'\033[0;0m'

usuario = getpass.getuser()
data_atual = date.today()
seuip = socket.gethostbyname(socket.gethostname())
print '-------------------------------------------'

print'\033[31m'+'Data:'+'\033[0;0m', (data_atual)
print '-------------------------------------------'
print'\033[31m'+'Hora:'+'\033[0;0m', now.hour
print '-------------------------------------------'
print'\033[31m'+'Minutos:'+'\033[0;0m', now.minute 
print '-------------------------------------------'
print'\033[31m'+'Segundos:'+'\033[0;0m', now.second
print '-------------------------------------------'
print'\033[31m'+'Usuário: '+'\033[0;0m', (usuario)
print '-------------------------------------------'
print'\033[31m'+'Sistema: '+'\033[0;0m', platform.system()
print '-------------------------------------------'
print'\033[31m'+'arquitetura do processador: '+'\033[0;0m', platform.machine()
print '-------------------------------------------'
print'\033[31m'+'Nome do computador: '+'\033[0;0m', platform.node()
print '-------------------------------------------'
print'\033[31m'+'Distribuição: '+'\033[0;0m',  platform.platform()
print '-------------------------------------------'
print'\033[31m'+'Processador: '+'\033[0;0m' 
os.system("cat /proc/cpuinfo | sed '5!d'")
print '-------------------------------------------'

print '-------------------------------------------'
print '\033[31m'+'Disco Rigído: '+'\033[0;0m' '\033[1;32m'
print '-------------------------------------------'
print""

def get_machine_storage():
    result=os.statvfs('/')
    block_size=result.f_frsize
    total_blocks=result.f_blocks
    free_blocks=result.f_bfree
    # giga=1024*1024*1024
    giga=1000*1000*1000
    total_size=total_blocks*block_size/giga
    free_size=free_blocks*block_size/giga
    print('Espaço total: %s' % total_size)
    print('Espaço livre: %s' % free_size)

get_machine_storage()
print '-------------------------------------------'
print'\033[31m'+'Seu ip: '+'\033[0;0m', (seuip)
print '-------------------------------------------'
print""
print""
print '\033[1;32m'+ (page)

