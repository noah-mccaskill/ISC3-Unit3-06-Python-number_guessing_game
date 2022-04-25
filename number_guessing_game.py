#!/usr/bin/env python3

# Created by: Noah McCaskill
# Created on: April 2022
# This is a guess the random number program

import random


def main():

    # This is a random number guesser, with try and catch

    # input
    guess_number_string = input("Enter your first guess here (0-9): ")
    random_Number = random.randint(0, 9)  # a number between 0 and 9

    # process & output
    try:
        guess_Number = int(guess_number_string)

        if guess_Number == random_Number:
            print("\nGuess is correct!")
        else:
            print("You guessed incorrectly")
            print("\nThe correct number is {0}.".format(random_Number))

    except Exception:
        print("\nThat was not an integer")
    print("\nDone.")


if __name__ == "__main__":
    main()
