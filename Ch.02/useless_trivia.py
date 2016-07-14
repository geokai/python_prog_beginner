#!/usr/local/bin/python3

# Useless Trivia

# Gets personal information form the user and then
# prints true but useless information about him or her:

import clear

clear.scrn_clr()

print ()
print ("Useless Trivia Game")
print ()

name = input ("Hello, Please enter your name: ")
age = int (input ("How old are you? "))
weight = int (input ("Okay, last question. How many pounds do you weigh? "))


print ("\nIf poet ee cumings were to email you , he'd address you as",
        name.lower())

print ("But if ee cumings were mad, he'd call you", name.upper())

called = name * 5
print ("\nIf a small child were trying to get your attention",)
print ("your name would become:")
print (called)

seconds = age * 365 * 24 * 60 * 60
print ("\nYou are over", seconds, "seconds old.")

moon_weight = weight / 6
print ("\nDid you know that on the moon you would weigh only", moon_weight,
        "pounds?")

sun_weight = weight * 27.1
print ("On the sun, you'd weigh", sun_weight, "(but, er... not for long).")

input ("\n\nPress the enter key to exit...")
clear.scrn_clr()

