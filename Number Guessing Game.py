# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 22:42:39 2018

@author: Nathan
"""
# Nathan Pan
# 7/16/2018
# Purpose: Create a game where the user must guess the number.

import random


#Takes the user's guess and displays the appropriate response
def userGuess():
    print("Let's play a game! I am thinking of a number between 1 and 100, try and guess what it is.")
    guesses = []
    guess_number = random.randint(0, 101) #can be changed to any number
    while True:
        guess = int(input("\nWhat is your guess?:"))
        if guess == guess_number:
            print("You got it! The number is " + str(guess) + "!")
            again = input("Would you like to play again? y/n: ").lower()
            if 'y' in again:
                userGuess()
            else:
                print("Thanks for playing!")
                break
        elif guess > guess_number:
            print("Sorry, you guessed too high! Try again.")
        elif guess < guess_number:
            print("Sorry, you guessed too low! Try again.")
        guesses.append(guess)
        strguesses = (", ".join(str(x) for x in guesses))
        print("Guesses: " + strguesses)
userGuess()
