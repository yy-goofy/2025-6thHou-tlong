#Name:Tristan long
#Class: 6th Hour
#Assignment: HW17
import random
#1. Create a def function that plays a single round of rock, paper, scissors where the user inputs
#1 for rock, 2 for paper, or 3 for scissors and compares it to a random number generated to serve
#as the "opponent's hand".
def rps():
    global comp
    user = int(input("Enter 1 for rock, 2 for paper, 3 for scissors: "))
    if user == 1:
        if user == 2:
            if user == 3:
                comp = random.randint(1, 3)
            print("you:", user)
        print("computer:", comp)
        if user == comp:
            print("tie")
        elif user == 1 and comp == 3:
            print("you win")
        elif user == 2 and comp == 1:
            print("you win")
        elif user == 3 and comp == 2:
            print("you win")
        else:
            print("you lose")
#2. Create a def function that prompts the user to input if they want to play another round, and
#repeats the RPS def function if they do or exits the code if they don't.
def play():
    again = "yes"
    while again == "yes":
        rps()
        again = input("play again? ").lower()