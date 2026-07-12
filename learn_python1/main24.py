questions= ("How many elements are there in periodic table?:",
            "Which animal lays the largest egg?: ",
            "What is the most abundant gas in Earth's atmosphere?: ")
options = (("a.116","b.117","c.118","d.119"),
         ("a.elephant","b.chicken","c.whale","d.ostrich"),
         ("a.nitrogen","b.oxygen","c.hydrogen","d.none"))
answers=("c","d","a")
guesses=[]
score = 0
question_num=0 # it work as index of list or tupple below 

for question in questions: #To display each question
    print("----------------------")
    print(question)
    for option in options[question_num]: # to display opeion and the loop continue until the question no. is;
        print(option)
    guess=input("Enter (A,B,C,D):").lower()# to display guesses and added to the list.
    guesses.append(guess)
    if guess== answers[question_num]: # to check that the guess is correct or not and count score.
        score+=1
        print("correct!")
    else:
        print("INcorrect!")
        print(f"{answers[question_num]} is the correst answer")
    question_num += 1



print("------RESULT---------")
print()
# to display andswe: correct answer.
print("answers:",end=" ")
for answer in answers:
    print(answer,end=" ")
print()

# similarly to display guesses by the user
print("guesses:",end=" ")
for guess in guesses:
    print(guess,end=" ")
print()

# to display soceres in percentage using formula.=obtain/total *100%
score=(score/len(questions)*100)
print(f"your score is {score:.2f}%")


print("THANK YOU FOR PLAYING YOU PLAYED WELL! ")