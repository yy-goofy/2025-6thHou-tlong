#Name:tristan long
#Class: 5th Hour
#Assignment: HW8

#1. Print "Hello World!"
print("hello world")
#2. Create 3 variables that each randomly generate a number between 1 and 10, named A, B, and C.
import random

A = random.randint(1, 10)
B = random.randint(1, 10)
C = random.randint(1, 10)

print(f"Variable A: {A}")
print(f"Variable B: {B}")
print(f"Variable C: {C}")
#3. Print A, B, and C on the same line.
print(A, B, C)
#4. Make an if statement that prints if variable A is greater than, less than, or equal to 5.
A = 7
if A > 5:
    print("Variable A is greater than 5")
elif A < 5:
    print("Variable A is less than 5")
else:
    print("Variable A is equal to 5")
#5. Make an if statement that prints if variable B is between 3 and 7, or not.
B = 5
if 3 <= B <= 7:
    print("Variable B is between 3 and 7.")
else:
    print("Variable B is not between 3 and 7.")
#6. Make an if statement that prints if variable C is even or odd.
C = 10
if C % 2 == 0:
    print(f"{C} is even.")
else:
    print(f"{C} is odd.")
#7. Create a variable whose value is 3 + a randomly generated number between 1 and 20
import random

random_number = random.randint(1, 20)
my_variable = 3 + random_number

print(f"The random number generated was: {random_number}")
print(f"The value of my_variable is: {my_variable}")
#8. Make an if statement that prints if the variable from #7 is greater than, less than, or equal to A + B + C.
variable_7 = 50
A = 10
B = 20
C = 30

sum_ABC = A + B + C

if variable_7 > sum_ABC:
    print("Variable from #7 is greater than A + B + C.")
elif variable_7 < sum_ABC:
    print("Variable from #7 is less than A + B + C.")
else:
    print("Variable from #7 is equal to A + B + C.")
