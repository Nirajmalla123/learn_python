# memebership operators =
# Used to test whether a value or variable found in a sequence.
# (satring,list,set,tuple,or dictionary)
# (1).in 
# (2).not in 

# word = "apple"
# letter = input("guess the letter in the secret word:")
# if letter in word:
#     print(f"yes '{letter}' found in the secret word")
# else:
#     print(f"{letter} was not found ")



students = {"hero":'A',"zero":'B',"biro":'C'}
student = input("enter the name of the student:")     
if student not in students:
    print("student was not fount:")
else:
    print(f"student name '{student} was found on the list and his/her grade is {students[student]}")
