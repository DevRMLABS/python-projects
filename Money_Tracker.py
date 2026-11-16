# This program tracks you incoming and outgoing expenses.
print("Hi welcome to the money tracker.")

balance = float(input("enter your balance: "))
spent = float(input("enter how much you spent: "))

remaining = balance - spent
print("your remainder is: $" , remaining)

if remaining < 100:
    print("warning! your balance is low.")
else:
    print("Your balance is looking good!")
