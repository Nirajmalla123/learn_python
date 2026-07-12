# Decorator= a function that extends the behavior of another function w/o modifying the base function.
# pass the base function as an argument to the decorator.
  
       # add_sprinkles
       # get_ice_cream("vanilla")
# def add_sprinkles(func):  # decorator function
#     def wrapper():        # we use this inner function to ensures the original function is only executed when we explicitly call it../// the inner function is used so the decorator can decide when and how to call the base function, instead of executing it immediately
#         print("you add sprinkles")
#         func()
#     return wrapper

# def add_fug(func):
#     def wrapper():        # this is so that we don't call this function when we apply decorator
#         print("you add fug")
#         func()
#     return wrapper

# @add_fug                   # another decorator
# @add_sprinkles             # decorator it automatically call/execute both addsprinkles function and geticecream function
# def get_ice_cream():       # base function
#     print("here is your ice cream")
# get_ice_cream()



# if our base function accept argument  like "flavor"

def add_sprinkles(func):  
    def wrapper(*args,**kwargs):      # this function isnot setup to accept argument .so use *arg and **kwarg  to accept any number of argument and keyword argument  
        print("you add sprinkles")
        func(*args,**kwargs)
    return wrapper

def add_fug(func):
    def wrapper(*args,**kwargs):        
        print("you add fug")
        func(*args,**kwargs)
    return wrapper

@add_fug                   
@add_sprinkles            
def get_ice_cream(flavor):      
    print(f"here is your {flavor} of ice cream")
get_ice_cream("vanilla")
