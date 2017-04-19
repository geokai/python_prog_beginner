#!/usr/local/bin/python3

import sys
sys.path.insert(0, "lib/modules")
import clear

# Quotation Manipulation:
# Demonstrates string methods:

clear.screen_clr ()

# quote from IBM Chairman, Thomas Watson, in 1943:
quote = "I think there is a world market for maybe five computers."

print ("Original quote:")
print (quote)

print ("\nIn uppercase:")
print (quote.upper())

print ("\nIn lowetcase:")
print (quote.lower())

print ("\nAs a title:")
print (quote.title())

print ("\nWith a minor replacement:")
print (quote.replace("five", "millions of"))

print ("\nOriginal quote is still:")
print (quote)

input ("\n\nPress the enter key to exit...")

clear.screen_clr ()
