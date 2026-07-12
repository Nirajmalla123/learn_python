# LIST COMPREHENSION
# a concise way to create lists 
# compact and easier to read tha traditional loops 
# formul use this - [expression for value in iterable if condition] 


doubles = []
for x in range (1,11):
    doubles.append(x*2)
print(doubles)         # we use list comprehensionn to make this above code more compact and easier to read.


doubles=[x*2 for x  in range(1,11)]
print(doubles)


fruits = ["apple","banana","coconut"]
fruit = [fruit.upper() for fruit in fruits]
print(fruit)


numbers = [1,2,3,4,-2,-3,-5]
number = [x for x in numbers if x>=0]
print(number)

negative_num=[x for x in numbers if x<0]
print(negative_num)