"""
                                   Snake Water Gun
1. Computer will select one from snake, water and Gun and same will be done by the user
2. snake - Water : Snake wins
   Snake - Gun : Gun wins
   Water - Gun : Water wins
3. This Game will be played 10 times. Who ever wins maximum number of time will be the winner
4. Print how many time computer wins and how many times the user wins
"""

import random
lst = ["Snake", "Water", "Gun"]

c = 0
u = 0
d = 0
i = 1
while i <= 10:
    cmp = random.choice(lst)
    n = input("Snake, Water or Gun? ")
    if n == cmp:
        print("Draw Match!!")
        print("Computer has selected: "+cmp)
        d = d + 1
        i = i + 1
    elif n == 'Snake' and cmp == 'Gun':
        print("Computer Wins!!")
        print("Computer has selected: " + cmp)
        c = c+1
        i = i + 1
    elif n == 'Gun' and cmp == 'Water':
        print("Computer Wins!!")
        print("Computer has selected: " + cmp)
        c = c + 1
        i = i + 1
    elif n == 'Water' and cmp == 'Snake':
        print("Computer Wins!!")
        print("Computer has selected: " + cmp)
        c = c + 1
        i = i + 1
    elif n == 'Snake' and cmp == 'Water':
        print("User Wins!!")
        print("Computer has selected: " + cmp)
        u = u + 1
        i = i + 1
    elif n == 'Water' and cmp == 'Gun':
        print("User Wins!!")
        print("Computer has selected: " + cmp)
        u = u + 1
        i = i + 1
    elif n == 'Gun' and cmp == 'Snake':
        print("User Wins!!")
        print("Computer has selected: " + cmp)
        u = u + 1
        i = i + 1
if u > c:
    print("******* Result *******")
    print("User has won the Game!!")
    print("User's point is ", u, "and Computer's point is", c)
elif u < c:
    print("******* Result *******")
    print("Computer has won the Game!!")
    print("User's point is", u, "and Computer's point is", c, "There are", d, "draw matches")
elif u == c:
    print("******* Result *******")
    print("Sorry!! Draw Match")
    print("User's point is ", u, "and Computer's point is", c)
