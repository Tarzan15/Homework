# -*- coding: utf-8 -*-
"""
Created on Sun Nov  5 12:52:22 2017

@author: JaceDonaldBroadbent
"""

print("I'm going to guess your number between 1 and 100, if my guess is correct, type 'Correct'")
print("if my guess is higher than your number type 'High'")
print("If it's lower than your number, press 'Low'")

lower_bound = 0
upper_bound = 100
number = int((upper_bound + lower_bound)/2)
done = False
tries = 0
guess = input(number)

while done != True:
        if guess == "High":
                upper_bound = number
                number = int((upper_bound + lower_bound)/2)
                guess = input(number)
        elif guess == "Low":
                lower_bound = number
                number = int((upper_bound + lower_bound)/2)
                guess = input(number)
        elif guess == "Correct":
                print("Nailed it! I got it in only", tries, "tries")
                done = True
        tries += 1
