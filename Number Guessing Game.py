import random

#Takes the user's guess and displays the appropriate response
def userGuess(guess_number):
    guess = int(input("What is your guess?:"))
    if guess == guess_number:
        print("You got it! The number is " + str(guess) + "!")
    elif guess > guess_number:
        print("Sorry, you guessed too high! Try again.")
    elif guess < guess_number:
        print("Sorry, you guessed too low! Try again.")
    return guess


def main():
    print("Let's play a game! I am thinking of a number between 1 and 100. Try and guess what it is.")
    guesses = []
    guess_number = random.randint(0, 101) #can be changed to any number
    again = "y"
    while(again == "y"):
        guess = userGuess(guess_number)
        guesses.append(guess)
        strguesses = (", ".join(str(x) for x in guesses))
        print("Guesses: " + strguesses)
        if guess == guess_number:
            again = input("Would you like to play again? y/n").lower()
            guesses = []
            guess_number = random.randint(0, 101)
        
main()
