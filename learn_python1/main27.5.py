# How to generate some random number in python.

import random

# number = random.randint(1,6) # choose random integer number between the given range
# # number=random.random() # return random float no. between 0 and 1
# print(number)


# options=("rock","paper","scissor")

# number = random.choice(options) #   Choose a random element from a non-empty sequence.
# print(number)


cards=["2","3","4","5","6","7"]
random.shuffle(cards)  #randomly suffle the list .
print(cards) 
