""" This program provides a simulation for a monty hall
problem of n doors, showing the expected value as well as
the experimental. This program assumes always switching. """
 
import random
won = 0
lost = 0
 
num = int(input("Number of Doors? "))
n = int(input("How many iterations? \n"))
 
def setup(): #creates random set of num doors
    car = random.randint(0, num - 1)
    doors = ["goat"] * num
    doors[car] = "car"
    return doors
 
for n in range(n):
    doors = setup()
    chosen = random.randint(0, num - 1) #chooses random door
    if doors[chosen] == "car": #if chosen is car then always lose (since always switching)
        lost += 1
    else:
        switch = random.randint(0, num - 3) #else there is 1/n-2 chance of selecting car (winning)
        if switch == 0:
            won += 1
        else:
            lost += 1
 
print("Switch \n")
print("Trials: " + str(won + lost))
print("Percentage Won: " + str(won/(won + lost) * 100))
print("Expected Win Percentage: " + str((num - 1)/(num * (num - 2)) * 100))
print("Percentage Lost: " + str(lost/(won + lost) * 100))

