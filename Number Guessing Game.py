# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 22:42:39 2018

@author: Nathan
"""
# Nathan Pan
# 7/16/2018
# Purpose: Create a game where the user must guess the number.

#Creates the number using some input from the user
def createNumber():
  print("To make the number, I need you to give me 3 integers from 1 to 10.")
  num1 = int(input("Number 1:"))
  while (num1 < 1 or num1 > 10):
    print("Pick a number between 1 and 10.")
    num1 = int(input("Number 1:"))
  num2 = int(input("Number 2:"))
  while (num2 < 1 or num2 > 10):
    print("Pick a number between 1 and 10.")
    num2 = int(input("Number 2:"))
  num3 = int(input("Number 3:"))
  while (num3 < 1 or num3 > 10):
    print("Pick a number between 1 and 10.")
    num3 = int(input("Number 3:"))
  guessNumber = ((num1 % 7) + 1) * num2 + (23 - num3)
  if guessNumber > 100:
    guessNumber = guessNumber - 100
  elif guessNumber < 0:
    guessNumber = guessNumber + 100
  return guessNumber

#Takes the user's guess and displays the appropriate response
def userGuess(guessNumber):
  guess = int(input("What is your guess?"))
  if guess == guessNumber:
    print("You got it! The number is " + str(guess) + "!")
    print("")
  elif guess > guessNumber:
    print("Sorry, you guessed too high! Try again.")
    print("")
  elif guess < guessNumber:
    print("Sorry, you guessed too low! Try again.")
    print("")
  return guess

def main():
  print("Let's play a game! I think of a number from 1 to 100, and you try to guess what it is.")
  again = "y"
  while(again == "y"):
    print("")
    guessNumber = createNumber()
    guess = userGuess(guessNumber)
    while(guess != guessNumber):
      guess = userGuess(guessNumber)
    again = input("Would you like to play again? y/n")

main()