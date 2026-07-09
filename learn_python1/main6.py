# while loop  = execute some code  infinite time unless the concition  is true. 

Age = int(input ("Enter your age :"))

while Age <=0:
 print(" you are not born yet or you are too old to be here so put valid age")
 Age = int(input ("Enter your age :"))
print(f"you are {Age} years old")