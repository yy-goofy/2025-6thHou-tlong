#Name:tristan long
#Class: 6th Hour
#Assignment: HW18
from random import random
import random
#1. Import the "random" library and create a def function that prints "Hello World!"
ran_list = []
def code():
    print("Hello world")
#2. Create two empty integer variables named "heads" and "tails"
heads = 0
tails = 0
#3. Create a def function that flips a coin one hundred times and increments the result in the above variables.
def coin_flip():
    player_call = int(input("1 for heads, 2 for tails"))
    coin_flip_result = random.randint(1,2)

    if coin_flip_result == player_call:
        print("You win!")
    else:
        print("You lose!")
        repeat_game()
def repeat_game():
        player_input = input("Do you want to play again? Y/N")

        if player_input == "Y" or player_input == "y":
            coin_flip()
        else:
            print("Thank you for playing!")
#4. Call the "Hello world" and "Coin Flip" functions here
code()
coin_flip()
#5. Print the final result of heads and tails here
print("head:", heads)
print("tail:", tails)
#6. Create a list called beanBag and add at least 5 different colored beans to the list as strings.
beanbag_list = ["Black Beans,Red Kidney Beans,White Navy/Cannellini Beans,Yellow Wax Beans,Green Mung Beans"]
#7. Create a def function that pulls a random bean out of the beanBag list, prints which bean you pulled, and then removes it from the list.
def bean():
    t = random.choice(beanbag)
    beanbag.remove(t)
    print('you removed that bean',t)
#8. Create a def function that asks if you want to pull another bean out of the bag and, if yes, repeats the #3 def function
def bean_pull():
    question = str(input("Do you want to go again? Y/N"))
    if question == "Y":
        bean()
#9. Call the "Bean Pull" function here
bean_pull()