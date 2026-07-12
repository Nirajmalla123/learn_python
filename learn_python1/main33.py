# Default argument = a default value for certain parameters
#                    default is use when that argument is omitted
#                    make your function  more flexible, reduces # of arguments 
#                    1.positionl, 2.Default, 3.keyword, 4.arbitrary
                
# 2.
# def net_price(list_price,discount=0.5,tax=0): # 1 is total discount
#     return list_price*(1-discount)*(1+tax)
# # print(net_price(500,0.5,0))
# print(net_price(500))

                                                             
        # EXERCISE
# CREATING COUNT UP TIMER
import time
def count (start,end):
    
    for x in range(start,end+1):
        print(x)
        time.sleep(1)
count(0,10)     #    it does three things in order:

                # Call the function count with arguments 0 and 10.

                # Execute the body of that function until it ends or hits a return.

                 # Produce a result — the return value of that function (default is None if no return is given).
print("DONE!")