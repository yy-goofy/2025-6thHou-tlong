#Name: tristan long
#Class: 6th Hour
#Assignment: HW_R8


#1. Import all of HW_R7 into this assignment using the from/import function.
from HWR7 import attributes
#2. Create an object of three students in the classroom. Ask for their name, grade, and favorite color as need be.
f = attributes(name="ally", grade=12, color="purple")
s  = attributes(name="greg", grade=12, color="purple")
t = attributes(name="alaya", grade=9, color="orange")

#3. Print the name of the first student.
print(f.name)
#4. Use the def function from HW_R7 to bump the grade level of the second student up by 1. Print the new grade.
s.add()
print(s.grade)
#5. Use the def function from HW_R7 to ask the third student to change their favorite color to something else.
#Print the new color.
print("the t student's new favourite color is", t.color)