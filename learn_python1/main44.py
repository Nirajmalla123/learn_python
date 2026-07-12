# PYTHON SLOT MACHINES
import random
def spin_row():
    symbols=['🔫','⭐','😎','❤️']
    return [random.choice(symbols) for symbol in range(3)]
def pnt_row(row):
    print("|".join(row))
def get_payout(row,bet):
    if row[0]==row[1]==row[2]:
        if row[0]=='🔫':
            return bet*2
        elif row[0]=='😎':
            return bet*3
        elif row[0]=='⭐':
            return bet*4
        elif row[0]=='❤️':
            return bet*10
    return 0
def main():
    balance=1000
    print("-------WELCOM TO PYTHON SLOT-------")
    print("Symbol:🔫⭐😎❤️")
    while balance>0:
        print(f"current balance is {balance}")
        bet=input("Enter your bet amount:")
        if not bet.isdigit():
            print("enter valid no.")
            continue
        bet=int(bet)
        if bet>balance:
            print("insufficient blc")
            continue
        if bet<=0:
            print("bet must be greater then zero")
            continue
        balance -=bet
        row = spin_row()
        pnt_row(row)
        payout= get_payout(row,bet)
         
        if payout>0:
            print(f"you won Rs{payout}")
            balance +=payout
        else:
            print("SORRY YOU LOSS!")
        
        again=input("DO YOU WANT TO PLAY AGAIN(Y/N):").upper()
        if again !='Y':
            break
    print(f"Game over! your final balance is {balance}")
       
   
if __name__ == "__main__":
    main()