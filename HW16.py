#Name:
#Class: 6th Hour
#Assignment: HW16
import random
#1. Create a def function that prints out "Hello World!"
def hello_world():
    print("Hello World!")
hello_world()
#2. Create a def function that calculates the average of three numbers (set the 3 numbers as your arguments).
def addition(a, b, c):
    d = (a+b+c)/3
    print(a, b , c)
    print(d)
#3. Create a def function with the names of 5 animals as arguments, treats it like a list, and
#prints the name of the third animal.
def animals(*animal):
    print(animals[2])
#4. Create a def function that loops from 1 to the number put in the argument.
def loop(number):
    for i in range(number):
        loop(i)
#5. Call all the functions created in 1 - 4 with relevant arguments.
hello_world()
addition(1, 2, 3)
animals("dog", "cat", "mouse, frog, lion, snake")
#6. Create a variable x that has the value of 2. Print x
x = 2
print(x)
#7. Create a def function that multiplies the value of 2 by a random number between 1 and 5.
def random_number():
    return random.randint(1, 5)
print(random_number())
#8. Print the new value of x.
print(x)
