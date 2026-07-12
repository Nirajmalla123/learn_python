# Number guessing game python

import random

lowest_num=1
highest_num=100
answer=random.randint(lowest_num,highest_num)
guesses=0

print("--------NUMBER GUESSING GAME------")
print(f"select a number between {lowest_num} and {highest_num}")

while True:
    guess=input("Enter your guess:")
    if guess.isdigit():
       guess=int(guess)
       guesses+=1
       if guess<lowest_num or guess>highest_num:
          print("that num is out of range")
          print(f"select a number between {lowest_num} and {highest_num}")
       elif guess<answer:
          print("too low! try again")
       elif guess>answer:
          print("too high try again!")
       else:
          print(f"correct! the answer was {answer}")
          print(f"Number of guess:{guesses}")
          break
    else:
      print("INVALID GUESS")
      print(f"select a number between {lowest_num} and {highest_num}")
     
    