# class variables in python:
# shared among all instances of a class
# Defined outside of the constructor
# allow you to share data among all object created from that class.


class student:
    class_year=2024                           #class variables
    num_student=0
    def __init__(self,name,age):              # constructor -> use to assign attribut 
        self.name=name                        # these are attribute
        self.age =age
        student.num_student+=1


student1=student("shyam",30)                 # objects
student2=student("hari",25)

print(student2.name)
print(student2.age)
print(student1.name)

print(student1.class_year)
print(student.num_student)