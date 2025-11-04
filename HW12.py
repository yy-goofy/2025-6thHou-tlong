#Name:Tristan long
#Class: 6th Hour
#Assignment: HW12

#1. Create a while loop with variable i that counts down from 5 to 0 and then prints
#"Hello World!" at the end.
i = 5
while i >= 0:
    print(i)
    i -= 1
#2. Create a while loop that prints only even numbers between 1 and 30 (HINT: modulo).
number = 1
while number <= 30:
    if number % 2 == 0:
        print(number)
    number += 1
#3. Create a while loop that prints from 1 to 30 and continues (skips the number) if the
#number is divisible by 3.
number = 1
while number <= 30:
    if number % 3 == 0:
        number += 1  # Increment before continuing to avoid infinite loop
        continue
    print(number)
    number += 1
#4. Create a while loop that randomly generates a number between 1 and 6, prints the result,
#and then breaks the loop if it's a 1.
import random

while True:
    # Generate a random number between 1 and 6 (inclusive)
    roll = random.randint(1, 6)
    print(f"The dice rolled: {roll}")

    # Check if the roll is 1 and break the loop if it is
    if roll == 1:
        print("Rolled a 1! Exiting the loop.")
        break
#5. Create a while loop that asks for a number input until the user inputs the number 0.
number = None  # Initialize number to a value other than 0 to enter the loop

while number != 0:
    try:
        number = int(input("Enter a number (enter 0 to stop): "))
    except ValueError:
        print("Invalid input. Please enter an integer.")

print("You entered 0. The loop has terminated.")
print(hello world)
