#Name:Tristan long
#Class: 6th Hour
#Assignment: HW15

#1. import the "random" library
import random
#2. print "Hello World!"
print("hello world")
#3. Create three variables named a, b, and c, and allow the user to input an integer for each.
A = int(input("enter number"))
B = int(input("enter number"))
C = int(input("enter number"))
#4. Add a and b together, then divide the sum by c. Print the result.
M = A + B
m = A
#5. Round the result from #3 up or down, and then determine if it is even or odd.
print(round(m))
#6. Create a list of five different random integers between 1 and 10.
int_list = [2, 4, 6 ,8, 1]
#7. Print the 4th number in the list.
print(8)
#8. Append another integer to the end of the list, also random from 1 to 10.
int_list.append(random.randint(1,10))
print(int_list)
#9. Sort the list from lowest to highest and then print the 4th number in the list again.
int_list.sort()
print(int_list)
print(int_list[0])
#10. Create a while loop that starts at 1, prints i and then adds i to itself until it is greater than 100.
import time
i = 1
while i <= 100:
    print(i)
    i += 1
#11. Create a list containing the names of five other students in the classroom.
class_list = ["Cash", "Alaya", "Tristan", "Devon", "ally"]
#12. Create a for loop that individually prints out the names of each student in the list.
class_list.sort()
print(class_list)
#13. Create a for loop that counts from 1 to 100, but ends early if the number is a multiple of 10.
i = 1
while i <= 100:
    print(i)
    i += 1
    if i * 10 == 0:
        continue
#14. Free space. Do something creative. :)