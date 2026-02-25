#   simulates an ATM

#   let's get the balance
name = input("Please enter your name to begin: ").strip().title()
balance = 1500

print(f"Hello, {name}! Welcome back to Python Bank.")
print(f"Your current balance is {balance:,}.")

#   now, let's make a transaction
confirmation = input("If you would like to withdraw more, type 'withdraw'. If you would like to instead deposit, type 'deposit'. ")
#   if confirmation equals yes
if confirmation == "withdraw":
    withdrawal = float(input("Please enter the amount you would like to withdraw: "))
    balance2 = balance - withdrawal
    print(f"Your new balance is: {balance2:,}.")
    #   making another transaction
if confirmation == "deposit":
    deposit = float(input("Please enter the amount you would like to deposit in: "))
    balance2 = balance + deposit
    print(f"Your new balance is {balance2:,}.")


receipt_confirmation = input("Would you like a receipt? Please type 'yes' or 'no'. ")
if receipt_confirmation == "yes":
    print(f"***Receipt for {name}.")
    print(f"Previous balance: {balance}.")
    # figure out how to show "Today's transactions", showing either the withdrawal amount or the deposit amount
    print(f"Your new balance is: {balance2}.")
    print("\nThank you for banking with Python Bank! See you again soon on the Terminal.")
if receipt_confirmation == "no":
    print("Thank you for banking with Python Bank! See you again soon on the Terminal.")

#   No need to use quotation marks and plus signs, it's a f string
#   {withdrawal} is a like a template for the value