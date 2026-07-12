# if_name_=_main_:
#  (this script can be iported or run standalone)
# [note]-> functions and classes in this module can be reused without the main block of code 
# makes our code more modular,
# helps readability, 
# leaves no global variables,
# avoid unintended execution. eg:library

def fav_food(food):
    print(f"fav food is {food}")

def main():
    print("this is script42a")
    fav_food("apple")
    print("good bye!")
if __name__=="__main__":
    main()