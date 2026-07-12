# super()= funtion used in a child class to call methods from a parent class (super class)
# allows you to extend the functionality of the inheritand methods.
# use to reuse the constructor of the parent class

class shapes:
    def __init__ (self,color,filled):
        self.color=color
        self.filled=filled
    def describe(self):                                    # method
         print(f"it is {self.color} and {self.filled}")

class circles(shapes):
    def __init__ (self,color,filled,radius):
        self.radius=radius
        super().__init__(color,filled)             # calling the construction i.e super class of shape
    def describe(self):                            # method overwriting
        print(f"it is a cicle with an area of {3.14*self.radius*self.radius} cm^2")
        super().describe()                         # accessing the describe method of parents

class squares(shapes):
     def __init__ (self,color,filled,width):
        super().__init__(color,filled)
        self.width=width
     def describe(self):                            # method overwriting
        print(f"it is a square with an area of {self.width*self.width} cm^2")   
        super().describe()

class triangles(shapes):
     def __init__ (self,color,filled,width,height):
        super().__init__(color,filled)
        self.width=width
        self.height=height
     def describe(self):                            # method overwriting
        print(f"it is a triangle with an area of {0.5*self.width*self.height} cm^2")

circle=circles("red",True,5)
square =squares("blue",False,6)
triangle= triangles("yellow",True,6,7)



print(circle.color)
circle.describe()
square.describe()
triangle.describe()