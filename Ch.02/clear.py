# this module determines the operating system type and provides the
# appropriate terminal scroll-back clearing (screen clear):

import os

def sceern_clr ():
    osname = os.name
    if osname == 'posix':
        os.system('clear')
    elif osname == 'nt' or osname == 'dos':
        os.system('cls')
    else:
        print("\n" * 30)
    return osname
