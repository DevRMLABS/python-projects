# This program asks for users paycheck amount, car payment, insurance payment, and how much you want to save.
print('hello its your computer here to help with your costs!')
print('now lets start of will your paycheck, describe your monthy paycheck.')
monthly_paycheck= float(input("What is your monthly paycheck?"))
print("Your paycheck is:", monthly_paycheck)
print("Alright, one step to the puzzle has been figured out by yours truly")
print("Right, now lets figure out your car payment!")
car_payment= float(input("How much is your car payment"))
print("great!! your car payment is:", car_payment)
print("Ok, what is your insurance payment on your vehicle")
insurance_payment= float(input("How much is your insurance payment?"))
print("Mkay, your insurance payment is:", insurance_payment)
print("Great lets now calculate your money left over")
money_left = monthly_paycheck - car_payment - insurance_payment
print("Ok, your left over money is:", money_left)
print('now thats explained tell me how much money you want to save?')
money_save=float(input("how much money do you want to save?"))
spendable_money = money_left - money_save
print("your spendable money is:", spendable_money)
