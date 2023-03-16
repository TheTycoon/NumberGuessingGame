# Number Guessing Game

import random

print("------------------------------------")
print("Welcome to the Number Guessing Game!")
print("------------------------------------")
print()

running = True
while running:
    number = random.randint(1, 10)

    guess = input("Guess a number between 1 and 10: ")
    print()

    if int(guess) == number:
        print("Congratulations! You guessed the correct number!")
        guess2 = 0
    elif int(guess) < number:
        guess2 = input("Your guess was too low, try again: ")
    elif int(guess) > number:
        guess2 = input("Your guess was too high, try again: ")
    else:
        guess2 = 0

    if int(guess2) == number and int(guess2) != 0:
        print("Congratulations! You guessed the correct number!")
    else:
        print("Sorry. Better luck next time. The number was %d." % number)

    print()
    again = input("Do you want to play again? (Type 'yes' or 'no') ")
    again = again.lower()
    if again != "yes":
        running = False
    else:
        print()
