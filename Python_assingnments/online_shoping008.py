amount = int(input("Enter the amount of your purchase: "))

if amount > 100:
    print(f"Congratulations! you've earned a 10% discount. Your final price is {amount * 0.9}")
elif amount <= 100 and amount > 50:
    print(f"You've earned a 5% discount. Your final price is {amount*0.95}")
else:
    print(f"No discount is applied. Your final price is {amount}")