#Typecasting: the process of converting a value of one datatype to another (string, integer , float, boolean) there are two way 
#  explicit and implicit
# explicit
name="Niraj"
age=24
gpa=2.9
student=True
print(type(name))
print(type(age))
print(type(gpa))
print(type(student))

#converting age int to float
age= float(age)
print(age)


#converting boolean to string
student = str(student)
print(student)
print(type(student))

#strint to boolean
name = bool(name)
print(name)


#str to boolean
age=bool(age)
print(age)




#2.implicit typecasting converting int into float.
x=2
y=7
x=x/y
print(x)