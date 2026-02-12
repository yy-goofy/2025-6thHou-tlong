#Name:Tristan long
#Class: 6th Hour
#Assignment: HW19

#1. Import the def functions created in problem 1-4 from HW16
from HW16 import hello_world, addition, animals ,loop
#2. Call the functions here and run HW19
"""
hello_world()
addition(1, 2, 3)
animals("dog", "cat", "mouse, frog, lion, snake")
loop(number)
"""
#3. Delete all calls for problem 5 in HW16 and run HW19 again.
print("got it")
#4. Create a try catch that tries to print variable x (which has no value), but prints "Hello World!" instead.
try:
    print(x)
except:
    print("Hello World!")
#5. Create a try catch that tries to divide 100 by whatever number the user inputs, but prints an exception for Divide By Zero errors.
try:
    num_div = int(input("Give me an integer: "))
    print(100/num_div)
except ZeroDivisionError:
    print("Cannot divide by zero!")
except ValueError:
    print("Value Error. Needs to be an integer!")
except:
    print("Unknown error.")
#6. Create a variable that asks the user for a number. If the user input is not an integer, prints an exception for Value errors.
try:
    k = int(input("Give me an integer"))
    print(k)
except:
    raise ValueError("It needs to be an integer!")
#7. Create a while loop that counts down from 5 to 0, but raises an exception when it counts below zero.
j = 10
while j >= 1:
    print(j)
    time.sleep(1)
    j -= 1
