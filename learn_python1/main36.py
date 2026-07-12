# Iterables = An object/collection that can return it's elements one at a time,
# allowing it to be iterated over in a  loop 

x = [1,2,3,4,5,6,7,8,9]
for y in reversed(x):
    print(y)


x = (1,2,3,4,5,6)
for y in x:
    print(y)

fruits={"banana","apple","coconut"}   # {stes}
for fruit in fruits:
    print(fruit)

names="niraj malla"    # string
for letter in names:
    print(letter,end=" ")

print()

my_dictionary = {"a":1,
                 "b":2,"c":3,"d":4,"e":5
                 }
for gu,value in my_dictionary.items():
    print(gu,value)