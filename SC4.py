#Name:Tristan long
#Class: 6th Hour
#Assigment: SC4


#After an extended leave, the team lead for the RPG developer is back, and he wants to continue the project.
#He wants to prototype the character creation model but first needs something that rolls stats for the characters.
#He wants you to make a function that rolls 4 six-sided dice (d6), sorts them from highest to lowest, and then adds the
#highest 3 together. He then wants you to add that result to a list outside the function. He wants you to run that function
#5 more times (six times total) and print all six stats.
import random
def func():
    s1 = random.randint(1, 6)
    s2 = random.randint(1, 6)
    s3 = random.randint(1, 6)
    s4 = random.randint(1, 6)
    s_list = [s1, s2, s3, s4]
    s_list.sort(reverse=True)
    t = s_list[0] + s_list[1] + s_list[2]
    stats.append(t)
def x():
    for y in range(1,7):
        func()

x()
print('stats')
#Once that is done, to ensure that the average of the stat block is fair (somewhere roughly between 12-13), he wants you
#to plug it into a calculator (SC5) and print the average.
print()