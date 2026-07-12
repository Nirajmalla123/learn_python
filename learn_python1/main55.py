# class methods = allow operations related to the class itself.
# -> Takes (cls) as the first paramethers which represent class itself. 
# -> best for class-level data or required access to class itself

class student:
    count=0
    def __init__(self,name,age):
        self.name=name
        self.age=age
        student.count+=1        # count the obj that are made by this class
    def getinfo(self):
        return f"{self.name}={self.age}"
    #class method
    @classmethod
    def getcount(cls):
        return f"total no of student: {cls.count}"
student1=student("hero",32)
student2=student("zero",82)
print(student.getcount())