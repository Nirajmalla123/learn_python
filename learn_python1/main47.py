# PYTHON OOP
# object = a "bundle" of related attributes (variables) and methods (function)
# ex. phone, cup, book
# you need a  'class' to create any object.

# class = (blueprint) used to design the structure and layout of any object.

from car47 import car

car1=car("mustang",2024,"red",False)           # objects
car2=car("corvette",2025,"blue",True)

print(car1.model)
print(car2.model)
print(car1.year)
print(car1.color)

# method

car2.drive()                
car1.stop()
car2.describe()