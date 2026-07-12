# magic methods = donder methods(double undrscore) __init__,__str__,__eq__,__lt__
# they are automatically called by  many of python's built-in operations.
# they allow developers to define or customize the behavior of objects.

class student:
    def __init__ (self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return f"name:{self.name}={self.age}"
    def __eq__(self,other):  # other object can be use 
        return self.name==other.name
    def __lt__ (self,other):
        return self.age<other.age

# to search for a keyword/parameters with in an object.
    def __contains__(self,keyword):
        return keyword in self.name


student1=student("hero",23)
student2=student("zero",42)

print(student1)

print(student1==student2)
print(student1>student2)

print("hero" in student1)