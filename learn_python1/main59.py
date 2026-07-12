#  exception handeling in python
# -> an event that interrupts the flow of a program (ZeroDivisionError,TypeError,ValueError)
#      1.try,2.except,3.finally

try:
    number=int(input("enter a number:"))
    print(1/number)
except ZeroDivisionError:
    print("you can divide by zero idiote!")
except ValueError:
    print("this is value error")
except Exception:
    print("something went wrong!")
finally:
    print("do some cleanup here")    # it always execute 