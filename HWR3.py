#Name:Tristan long
#Class: 6th Hour
#Assignment: HW-R3


#1. import random and print "Hello World!"
import random
print("hello world")
#2. Create three variables that each randomly generate an integer between 1 and 10, print each number on the same line.
a = random.randint(1,10)
b = random.randint(1,10)
c = random.randint(1,10)
print(a,b,c)
#3. Create a list containing 5 strings listing 5 colors.
strings_list = ["blue,green,pink,red,purple"]
print(strings_list)
#4. Use a function to randomly choose one of the 5 colors from the list and print the result.
print(random.choice(strings_list))
#5. Create an if statement that determines which of the three variables from #2 is the lowest.
if a <= b and a <= c:
    print(f"a is the lowest number with {a}")
if b <= a and b <= c:
    print(f"b is the lowest number {b}")
if c <= b and c <= a:
    print(f"c is the lowest number{c}")
if a == b == c:
    print("all are equal")