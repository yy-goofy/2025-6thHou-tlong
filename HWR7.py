#Name: tristan long
#Class: 6th Hour
#Assignment: HW_R7


#1. Create a class containing a def function that inits self and the three attributes: name, grade, color.
class attributes:
    def __init__(self, name, grade, color):
        self.name = name
        self.grade = grade
        self.color = color
    def add(self):
        self.grade += 1
        if self.grade == 12:
            print("your down")
        else:
            self.grade += 1
            print('your in the', self.grade, 'grade')
    def change(self):
        t =imput('change your favourite color!: yes/no')
        if t == 'yes':
            slef.color = imput ('what would you like to change your favourite color to?')
print(attributes.__doc__)

#2. Make a def function within the class that adds 1 to the grade attribute to any object called to it.
#If they are 12th grade, have the code change their grade to "graduated" instead.

#3. Make a def function within the class that offers the user to input/change their favorite color.