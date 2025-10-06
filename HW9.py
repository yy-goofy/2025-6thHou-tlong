#Name:tristan long
#Class: 6th Hour
#Assignment: HW9


#1. Print "Hello World!"
print("hello world")
#2. Create a list with three variables that each randomly generate a number between 1 and 100
import random

variable1 = random.randint(1, 100)
variable2 = random.randint(1, 100)
variable3 = random.randint(1, 100)

random_numbers_list = [variable1, variable2, variable3]

#3. Print the list.
print(random_numbers_list)
#4. Create an if statement that determines which of the three numbers is the highest and prints the result.
num1 = 10
num2 = 25
num3 = 15

if num1 >= num2 and num1 >= num3:
    print(f"{num1} is the highest number.")
elif num2 >= num1 and num2 >= num3:
    print(f"{num2} is the highest number.")
else:
    print(f"{num3} is the highest number.")
#5. Tie the result (the largest number) from #4 to a variable called "num".
data_list = [4, 1, 9, 7]

number = max(data_list)
print(number)
#6. Create a nested if statement that prints if num is divisible by 2, divisible by 3, both, or neither.
num = 12

if num % 2 == 0:
    if num % 3 == 0:
        print(f"{num} is divisible by both 2 and 3.")
    else:
        print(f"{num} is divisible by 2 but not by 3.")
else:
    if num % 3 == 0:
        print(f"{num} is divisible by 3 but not by 2.")
    else:
        print(f"{num} is neither divisible by 2 nor by 3.")