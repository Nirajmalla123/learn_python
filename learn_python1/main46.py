#HANGMAN PROGRAM IN PYTHON

import random
from WORDhangman import words

han_guess={
    0:("   ",
       "   ",
       "   "
    ),
    1:(" O ",
       "   ",
       "   "
    ),
    2:(" O ",
       " | ",
       "   "
    ),
    3:(" O ",
       "/| ",
       "   "
    ),
    4:(" O  ",
       "/|\\",
       "    "
    ),
    5:(" O  ",
       "/|\\",
       "/   "
    ),
    6:(" O  ",
       "/|\\",
       "/ \\"
    ),
}
# for line in han_guess[6]:
#     print(line)

def display_man(wrong_guesses):
    for line in han_guess[wrong_guesses]:
        print(line)
def display_hint(hint):                            # DEFINING NECESSARY FUNCTION
        print(" ".join(hint))
def display_answer(answer):
         print(" ".join(answer))
def main():
    answer=random.choice(words)
    hint=["_"]*len(answer)
    wrong_guesses=0                                 # DECLARING NECESSARY VARIABLE 
    guess_letter=set()
    is_running= True
    while is_running:

        display_man(wrong_guesses)
        display_hint(hint)
        guess=input("Enter a letter:").lower() 

        if len(guess)!=1 or not guess.isalpha():
             print("INVALID INPUT!")
             continue                                              # INPUT VALIDATION OF GUESS FROM USER        
        if guess in guess_letter:
             print("it is already guessed:")
             continue
        
        guess_letter.add(guess)

        if guess in answer:
            for i in range(len(answer)):
                 if answer[i] == guess:                            # REPLACING HINT WITH THE CORRECT GUESS/ ANSWER
                      hint[i]=guess
        else:
             wrong_guesses +=1   

        if "_" not in hint:
             display_man(wrong_guesses)
             display_answer(answer)
             print("YOU WIN!")
             is_running = False                                # DISPLAYING YOU WIN OR LOSS WITH THE HELP OF _ AND WRONG GUESSES
        elif wrong_guesses>=6:                                        
             display_man(wrong_guesses)
             display_answer(answer)
             print("YOU LOSE!")
             is_running = False

if __name__=="__main__":
    main()