# 2d-list = it is a list made up of lit inside.


fruits = ["apple","banana","pineapple"]
vegetables= ["carrot","potato","cauliflower"]
meats=["fish","chicken","buff"]

groceries=[fruits,vegetables,meats]
print(groceries [0][0])                                   # for index remember it like matrix start from 0,0  

# to iterate all the vale in the 2d list use nested loop  

groceries1=[ ["apple","banana","pineapple"],["carrot","potato","cauliflower"],["fish","chicken","buff"]]


for i in groceries1:
    for ii in i:
        print(ii)


        # ceate 2d keypad( it should be in ordered so use tupple)
        
num_pad = ((1,2,3),
           (4,5,6),
           (7,8,9),
           ("*",0,"#"))

for row in num_pad:
  for num in row:
     print(num,end=" ")
  print()