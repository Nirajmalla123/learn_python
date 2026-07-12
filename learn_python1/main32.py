# Function() = A block of reusable code place() after the function name to invoke it.
# syntax: def function_name():

# def happ_bdy(you):
#      print("Happy bdy to you!")
#      print("Happy bdy to you!")
#      print(f"happy bdy to {you}")
#      print()
# happ_bdy("bro")
# happ_bdy()


# def display_invoice (username,amount,due_date):
#     print(f"Hello {username}")
#     print(f"your bill of Rs{amount:.2f} is due: {due_date}")

# display_invoice("Bro",2500,"01/12")

# Return statement = is used to end a function and send a result back to the caller.

def add(x,y):
   z=x+y
   return z

def sub(x,y):
   z=x-y
   return z

def mult(x,y):
   z=x*y
   return z
print(add(1,3))
print(sub(8,3))
print(mult(12,12))



#little advance 
def create(first,last):
   first = first.capitalize()
   last = last.capitalize()
   return first +" "+ last # to concatination string use  one +. if you want space inbetween then use +" "+
full_name= create("hero","hero")
print(full_name)