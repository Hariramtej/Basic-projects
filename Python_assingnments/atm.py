withdraw = int(input("Enter the amount you want to withdraw: "))
acc_balance = int(input("Enter your account balance: "))

if withdraw <= acc_balance:
    if acc_balance < 100:
        if withdraw > 50:
            print("You cannot withdraw more than $50")
        else:
            print("You have succesfully withdrawed the money")
    if withdraw < 500:
        print(f"You have succesfully withdrawed ${withdraw}")
    elif withdraw < 1000:
        print(f"You have succesfully withdrawed ${withdraw}. You were added $10 as service charge.")
    elif withdraw > 1000:
        print(f"You have succesfully withdrawed ${withdraw}. You were added $25 as service charge.")