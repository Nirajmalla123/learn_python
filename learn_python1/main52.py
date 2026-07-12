# Polymorphism = greek word that means to have many forms or faces
         # poly= many and morphe= form
# two ways to  achieve polymorphism
#    1.inheritance= an object could be treated of the same type as a parent class 
#    2."duck typing" = object must have necessary attribute/methods

# 1. 
from abc import ABC, abstractmethod
class shape:
  @abstractmethod
  def area(self):
    pass  
class circles(shape):
  def __init__ (self,radius):
   self.radius = radius
  def area(self):
    return 3.14*self.radius**2
class squares(shape):
  def __init__ (self,side):
     self.side=side
  def area(self):
    return self.side*self.side
class triangles(shape):
  def __init__ (self,width,height):
    self.width=width
    self.height=height
  def area(self):
    return f"the area of triangle is {0.5*self.width*self.height}"
  
class hero(circles):                                  
  def __init__ (self,topper,radius):
     self.topper=topper
     self.radius=radius
 
shap=[circles(4),squares(3),triangles(2,3),hero("topper",31)]  # here hero object have many form it is also shape and circle so it is polymorphism

for sha in shap:
  print(sha.area())
