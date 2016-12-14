#!/usr/local/bin/python3

import sys
sys.path.insert(0, "lib/modules")
import clear

# Fancy Credits
# Demonstrates escape sequences

clear.screen_clr ()

print ("\t\t\tFancy Credits")

print ("\t\t\t \\ \\ \\ \\ \\ \\ \\")
print ("\t\t\t      by")
print ("\t\t\tMicheal Dawson")
print ("\t\t\t \\ \\ \\ \\ \\ \\ \\")

print ("\nSpecial thanks goes out to:")
print ("My hair stylist, Henry \'The Great,\' who never says \"can\'t.\"")

# sound the system bell:
print ("\a")

input ("\n\nPress the enter key to exit...")
print ()
print ()
clear.screen_clr ()
