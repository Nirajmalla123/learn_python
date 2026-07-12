# property decorator = used to define a method as a property (it can be access like a attribute)
# benefit:add additional logic when write or delete attributes 
# -> Gives you gatter,setter and deleter method.

class Rectangle:
    def __init__ (self,width,height):
        self._width=width              # _ these attribut ment to be privet so ment to be use unter the class only 
        self._height=height
    @property                            # gatter
    def width(self):
        return f"{self._width:.1f}cm"
    @property
    def height(self):
        return f"{self._height:.1f}cm"
    
    @ width.setter                           # setter
    def width(self,new_width):
        if new_width>0:
            self._width=new_width
        else:
            print("width must be greater then zeero")
    @ height.setter
    def height(self,new_height):
        if new_height>0:
            self._height=new_height
        else:
            print("height must be greater then zero")
    
    @width.deleter
    def width(self):
        del self._width
        print("the width is deleted")

rectangle1=Rectangle(3,4)

rectangle1.width=0
rectangle1.height=6
del rectangle1.width

# print(rectangle1._width)
print(rectangle1._height)


