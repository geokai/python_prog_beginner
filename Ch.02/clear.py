# this module determines the operating system type and provides the
# appropriate terminal scroll-back clearing (screen clear):

import os

def screen_clr ():
    osname = os.name
    if osname == 'posix':
        os.system('clear')
    elif osname == 'nt' or osname == 'dos':
        os.system('cls')
    else:
        print("\n" * 30)
    return osname

if __name__ == "__main__":
    screen_clr ()

