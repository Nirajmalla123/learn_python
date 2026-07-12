# Nested loop = A loop within another loop (outer,innter)
#           outer loop:
#             innter loop:

row=int(input("Enter the rows of rectangle:"))
column= int(input("Enter a column of a rectangle:"))
symbol= input("Enter the symbols to use in rectangel:")

for x in range(row):
    for y in range(column):
        print(symbol,end="")
    print()