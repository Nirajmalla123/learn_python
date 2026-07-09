# python compound ineres calculator

principle=0 
rate=0 
time=0

while principle<=0 :
    principle=float(input("enter your initial balcnce :"))
    if principle<=0 :
     print("principle can't be negative or zero")

while rate<=0 :
   rate=float(input("enter your interest rate :"))
   if rate<=0 :
     print("rate can't be negative or zero")

while time<=0 :
   time=int(input("enter your time in years :"))
   if time<=0 :
     print("time can't be negative or zero")

total= principle*pow((1+rate/100),time)
print(f"your total balance after {time} years is Rs {total:,.1f}")

