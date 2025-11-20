#Name:Tristan long
#Class: 6th Hour
#Assignment: SC3

#You have been transferred to a new team working on a mobile game that allows you to dress up a
#model and rate other models in a "Project Runway" style competition.

#They want to start prototyping the rating system and are asking you to make it.
#This prototype needs to allow the user to input the number of players, let each player rate
#a single model from 1 to 5, and then give the average score of all the ratings.

players = int(input("how many players? : "))
total = 0
for x in range(players):
    rating = int(input("Enter rating : "))
    total += rating
    while rating > 5 or rating < 1:
        print("not a valid rating")
        rating = int(input("Enter rating : "))
    else :
        total += rating
print(total / players)
