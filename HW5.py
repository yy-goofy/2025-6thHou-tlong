#Name:Tristan long
#Class: 6th Hour
#Assignment: HW5


#1. Create a list with 9 different numbers inside.
number_list = [1,2,3,4,5,6,7,8,9]
#2. Sort the list from highest to lowest.
number_list.sort(reverse=True)
#3. Create an empty list.
hw_list = []
#4. Remove the median number from the first list and add it to the second list.
kenku=number_list[4]
number_list.pop(4)
hw_list.append(kenku)
#5. Remove the first number from the first list and add it to the second list.
rogue=number_list[0]
number_list.pop(0)
hw_list.append(rogue)
#6. Print both lists.
print(number_list)
print(hw_list)
#7. Add the two numbers in the second list together and print the result.
gg=hw_list[0]+hw_list[1]
print(gg)
#8. Move the number back to the first list (like you did in #4 and #5 but reversed).
number_list.append(gg)
hw_list.pop(0)
hw_list.pop(0)
#9. Sort the first list from lowest to highest and print it.
number_list.sort()
print(number_list)