class_srevice = input("Enter the class[Economy, Business, First]: ").lower()
age = int(input("Enter your age: "))
amount = int(input("Enter the total ticket price: "))

if class_srevice == "economy":
    if age < 12:
        amount *= 0.7
    elif age >= 65:
        amount *= 0.8
elif class_srevice == "business":
    if age < 12:
        amount *= 0.6
    elif age >= 65:
        amount *= 0.75
else:
    if age < 12:
        amount *= 0.5
    elif age >= 65:
        amount *= 0.3

print(f"Your final ticket price is {amount}")