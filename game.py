print("welcome player")

import random

def guess_the_number():
    """A simple 'Guess the Number' game."""
    print("Welcome to Guess the Number!")
    print("I'm thinking of a number between 1 and 100.")
    print("You have 7 attempts to guess it.")

    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 7

    while attempts < max_attempts:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < secret_number:
                print("Too low!")
            elif guess > secret_number:
                print("Too high!")
            else:
                print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
                return # End the game

        except ValueError:
            print("Invalid input. Please enter a whole number.")

    print(f"Game over! You ran out of attempts. The secret number was {secret_number}.")

# Run the game
guess_the_number()