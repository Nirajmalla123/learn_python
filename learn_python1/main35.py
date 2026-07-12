# 4.Arbitary argument
#  *args=allows you to pass multple non-key arguments,we treat this as tupple
# **kwargs= allow you to pass multiple keyword-arguments

# def add(a,b):
#     return a+b
# print(add(1,2,4))

# def addition(*adds):
#     x=0
#     for add in adds:
#         x+=add
#     return x
# print(addition(1,2,4,5)) 


def display_name(*args):
    for arg in args:
        print(arg,end=" ")
display_name("dr.","vim","dhamala","hamala")
print()
# **kwargs = we treat this as dictionary (key:value)

def address(**kwargs):
    for kwarg,value in kwargs.items():# for value use kwargs.values(), and for key use kwargs.keys()
        print(f"{kwarg}:{value}")
address(street="fake one",
        city="banke",
        zip="13435")


def shipping_label(*args,**kwargs):
    for arg in args: # watch vdo
        print(arg)
shipping_label("book","hello","zero",
              street="fake one",
              city="banke",
              zip="13435")
