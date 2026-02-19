#Name:
#Class: 5th Hour
#Assignment: HW21

#1. Import the random and time libraries
import random
import time
#2. Create a class containing a def function that init's self and the 3 attributes health, damage, and speed.
class warrior:
    def __init__(self, health, damage, speed):
        self.health = health
        self.damage = damage
        self.speed = speed
    def warrior_loop(self):
        while x in range(10):
            warrior.health = warrior.health + random.randint(1,6)
            print('the warrior new health is', warrior.health)
            time.sleep(1)
#3. Make a "warrior" character object with 100 health, 20 damage, and 30 speed. Print the character's initial health below.
Ares = warrior(100, 20, 30)
print(warrior.health)
#4. Make a def function within the class that loops 10 times. Within this function,
#make the following loop 10 times: the character takes a random amount of damage from 1 to 6,
#the new health is printed, a time.sleep delay of one second is done. Call the function to the warrior.
warrior.warrior_loop()
print(warrior_loop)
#5. Make a "healer" character object with 60 health, 10 damage, and 30 speed.
healer = warrior(60, 10, 30)
#6. Make a def function within the class that heals the warrior for 30 health. Create an if statement
#that sets the warrior's health to its max (100) if the healing would bring the warrior's health above that.
#Call the function to the healer.
def healer_warrior():
    for x in range(10):
        warrior.health = healer.health + random.randint(1,30)
#7. Print the warrior's final health at the very bottom.
print(warrior.health)
