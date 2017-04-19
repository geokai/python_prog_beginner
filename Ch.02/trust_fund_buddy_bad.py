#!/usr/local/bin/python3

# Trust Fund Buddy - Bad
# Demonstrates a logical error:

import sys
sys.path.insert(0, "lib/modules")
import clear

clear.screen_clr()
print (
""" 
       Trust Fund Buddy 

Totals your monthly spending so that your trust fund doesn't run out
(and you're forced to get a real job).

Please enter the requested, monthly costs. Since you're rich, ignore pennies and
use only dollar amounts.

""" 
)

car = input ("Lamborghini Tune-Ups: ")
rent = input ("Manhattan Apartment: ")
jet = input ("Private Jet Rental:")
gifts = input ("Gifts: ")
food = input ("Dining Out: ")
staff = input ("Staff (butlers, chefs, driver, assistant): ")
guru = input ("Personal Guru and Coach: ")
games = input ("Conputer Games: ")

total = car + rent + jet + gifts + food + staff + guru + games

print ("\nGrand Total:", total)

input ("\n\nPress the enter key to exit...")
clear.screen_clr()

