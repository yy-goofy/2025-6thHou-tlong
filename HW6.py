#Name:
#Class: 6th Hour
#Assignment: HW6


#1. Import the "random" library
import random
from ctypes.wintypes import VARIANT_BOOL

#2. print "Hello World!"
print ("hello world")
#3. Create three different variables that each randomly generate an integer between 1 and 10
random1 = random.randint(1,10)
random2 = random.randint(1,10)
random3 = random.randint(1,10)
#4. Print the three variables from #3 on the same line.
print (random1, random2, random3)
#5. Add 2 to the first variable in #3, Subtract 4 from the second variable in #3, and multiply by 1.5 the third variable in #3.
add = random1 + 2
sub = random2 - 4
mul = random3 * 1.5
#6. Print each result from #5 on the same line.
print(add, sub, mul)
#7. Create a list containing four variables that each randomly generate an integer between 1 and 6
var_list = [random.randint(1,6), random.randint(1,6), random.randint(1,6), random.randint(1,6)]
#8. Sort the list in #7 and print it.
var_list.sort()
print(var_list)
#9. Add together the highest three numbers in the list from #7 and print the result.
print(var_list[1]+var_list[2]+var_list[3])
#10. Create a list with 5 names of other students in this class and print the list.
name_list=["ethan", "connor", "tristan", "cash", "greg"]
print(name_list)
#11. Shuffle the list in #10 and print the list again.
random.shuffle(name_list)
print(name_list)
#12. Print a random choice from the list of names from #10.
print(random.choice(name_list))