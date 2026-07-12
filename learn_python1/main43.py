# Python Baning program

def show_balance(balance):
    print(f"your current balance is Rs.{balance:.2F}")
    return 0
def deposit():
    amount=float(input("Enter the amount to be deposited:"))
    if amount<=0:
        print("this amount cann't be deposited,it should not be less or equal to zero ")
        return 0
    else:
        return amount
def withdraw(balance):
    amount=float(input("enter the abount to be withdraw:"))
    if amount>balance:
        print("INSUFFICIENT BALANCE!")
        return 0
    elif amount<0:
        print("amount must be greater then zero")
        return 0
    else:
        return amount

def main():
    is_running = True   
    balance = 0    
    while is_running:
        print("BANKING PROGRAM")
        print("1.show balance")
        print("2.deposit")
        print("3.withdraw")
        print("4.exit")
        
        choice = input("Enter your choice(1-4):")

        if choice=='1':
            show_balance(balance)
        elif choice=='2':
            balance += deposit()
        elif choice=='3':
            balance -= withdraw(balance)
        elif choice == '4':
            is_running = False
        else:
            print("please enter the valid choice!")

if __name__=='__main__':
   main()

print("THANK YOU! AND HAVE A NICE DAY!")