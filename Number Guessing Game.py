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

#Creates the random number depending on what range the user would like
def createNumber():
    low = int(input("What would you like the lowest number to be?"))
    high = int(input("What would you like the highest number to be?"))
    guess_number = random.randint(low, high)
    print("I am thinking of a number between " + str(low) + " and " + str(high) + ". Try and guess what it is!")
    return guess_number


def main():
    print("Let's play a game! You give me two numbers, and I will come up with a number between them. Try and guess what the number is.")
    guesses = []
    guess_number = createNumber()
    again = "y"
    while(again == "y"):
        guess = userGuess(guess_number)
        guesses.append(guess)
        strguesses = (", ".join(str(x) for x in guesses))
        print("Guesses: " + strguesses)
        if guess == guess_number:
            again = input("Would you like to play again? y/n").lower()
            if again == "y":
                guesses = []
                guess_number = createNumber()
            else:
                exit               
        
main()
