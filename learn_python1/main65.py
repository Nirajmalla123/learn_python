# Multithereading = used to perform multiple task concurrently (multitadking)
# -> Good for I/O bound tasks like reading files or fetching data from APIs.
#    threading.Thread(target=function_name,args=(parameter,))  # if you want to pass only one parameter then you must end with ',' to let know that it is tupple for python.


import threading
import time


def washing_cloth(name):        # if you want to pass 1 parameter
    time.sleep(8)
    print(f"you finish washing {name}")

def walk_dog():
    time.sleep(3)
    print("you finsh walking dog")

def  take_out_trash():
    time.sleep(4)
    print("you finish taking  out the trash")


# washing_cloth()
# walk_dog()
# take_out_trash()

chore1=threading.Thread(target=washing_cloth,args=("shirt",))         #  so 1 parameter then we can pass one argument
chore1.start()

chore2=threading.Thread(target=walk_dog)                        # [note] -> whoever takes less time threading execute that task 1st.
chore2.start()

chore3=threading.Thread(target=take_out_trash)
chore3.start()

chore1.join()                                 
chore2.join()                                    # join execute the above task first then only proceed to down below task i.e print
chore3.join()



print("all chores are complete")         #[ it take less time so it will execute 1st if we don't use join]