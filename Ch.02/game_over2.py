#!/usr/local/bin/python3

# Game Over - Version 2

# Demonstrates the use of quotes in strings


# import os
import clear

# def scrn_clr ():
#     osname = os.name
#     if osname == 'posix':
#         os.system('clear')
#     elif osname == 'nt' or osname == 'dos':
#         os.system('cls')
#     else:
#         print("\n" * 30)
#     return osname



clear.scrn_clr ()
print ()

# term_name = scrn_clr ()
# print (term_name)

print ("Program 'Game Over' 2.0")

print ("Same", "message", "as before")

print ("Just",
       "a bit",
       "bigger")

print ("Here", end=" ")
print ("it is...")

print (
        """
                _____       ___       ___  ___   _____  
               /  ___|     /   |     /   |/   | |  ___| 
               | |        / /| |    / /|   /| | | |__   
               | |  _    / ___ |   / / |__/ | | |  __|  
               | |_| |  / /  | |  / /       | | | |___  
               \_____/ /_/   |_| /_/        |_| |_____| 

                _____    _     _    _____    _____    _ 
               /  _  \  | |   / /  |  ___|  |  _  \  | |
               | | | |  | |  / /   | |__    | |_| |  | |
               | | | |  | | / /    |  __|   |  _  /  |_|
               | |_| |  | |/ /     | |___   | | \ \   _ 
               \_____/  |___/      |_____|  |_|  \_\ |_|

        """
        )

input ("\n\nPress the enter key to exit...")
print ()
print ()
clear.scrn_clr ()

