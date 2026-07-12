# 3. keyword argument = eg: end,sep
# an argument preceded by an identifier
# helps with readability
# order of argument doesn't matter

def hello(greeting,title,first,last):
    print(f"{greeting} {title} {first} {last}")
# hello("hi","mr","niraj","malla") # so this is positional argument
hello("hey",first="malla",title="mr.",last="niraj") # this is keyword argument.
