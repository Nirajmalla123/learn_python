#  for loop = execute a block of code a fixed number of times 
#  you can iterate over a range,string,sequence etc.

for count in range (1,11):
 print(count)


credit_card = "2434-230-2343-23-23"
for x in credit_card:
 print(x)

for x in range(2,9):
  if x==5:
   continue
  else:
   print(x)