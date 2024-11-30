import time
import datetime

print("Please Enter Your Card")

time.sleep(3)

user_pin = 1111
pin = int(input("Please Enter Your Card PIN : "))
print("=" * 50)


def atm():
    balance = 10000
    trans_history = []

    def transaction_logs(operation,amount):
        timestamp = datetime.datetime.now().strftime("%c")
        if amount > 0 :
            trans_history.append(f"{timestamp} -- {operation} - {amount}/-")


    while True:
        print("Welcome")
        print("""
            1 == Check Balance
            2 == Withdraw Amount
            3 == Deposit Amount
            4 == Transaction History
            5 == Exit
            """)
        ch = int(input("Enter Your Choice to Perform Operation : "))
        print("=" * 50)
        time.sleep(2)

        if ch == 1:
            print(f"Your Current Balance Is : {balance}/-")
            print("=" * 50)
            time.sleep(2)

        elif ch == 2:
            try:
                amount = float(input("Amount To Withdraw : "))
                if amount > balance:
                    print("Insufficient Balance")
                    print("=" * 50)
                    time.sleep(2)
                elif amount <= 0:
                    print("Enter A Valid Amount")
                    print("=" * 50)
                    time.sleep(2)
                else:
                    balance -= amount
                    transaction_logs("Withdraw",amount)
                    print(f"Amount {amount}/- Successfully Withdrawn.")
                    print(f"Current Balance Is {balance}/-")
                    print("=" * 50)
                    time.sleep(2)
            except ValueError:
                print("INVALID AMOUNT. Please Enter")
                print("=" * 50)
                time.sleep(2)

        elif ch == 3:
            try:
                amount = float(input("Amount To Deposit : "))
                if amount <= 0:
                    print("Enter A Valid Amount")
                    print("=" * 50)
                    time.sleep(2)
                else:
                    balance += amount
                    transaction_logs("Deposit",amount)
                    print(f"Amount {amount}/- Successfully Deposited.")
                    print(f"Current Balance Is {balance}/-")
                    print("=" * 50)
                    time.sleep(2)
            except ValueError:
                print("INVALID AMOUNT. Please Enter Numeric Value.")
                print("=" * 50)
                time.sleep(2)

        elif ch == 4:
            try:
                if trans_history is not None:
                    print("Transaction History : ")
                    for e in trans_history:
                        print(e)
                    print("=" * 50)
                    time.sleep(2)
                else:
                    print("No Transaction History")
                    print("=" * 50)
                    time.sleep(2)
            except:
                print("Error Loading Transaction History..Try Again")
                time.sleep(2)

        elif ch == 5:
            print("""Process Ended..
                     Thank You..""")
            print("=" * 50)
            print("=" * 50)
            break
        else:
            print("Please Select Valid Option.")
            print("=" * 50)
            print("=" * 50)
            time.sleep(2)

    return 0

if user_pin == pin :
    time.sleep(2)
    print("PIN Accepted")
    print("=" * 50)
    atm()
else:
    print("Invalid or Wrong PIN."
          "Try Again Please")
    print("=" * 50)
    time.sleep(2)
