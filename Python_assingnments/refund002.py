no_of_days = int(input("Enter no of days: "))
p_type = input("Is the product bought in clearance sale or limited edition[y/n]: ").lower()
p_damage = input("Is the product damaged[y/n]: ").lower()

if p_damage == "y":
    print("You will be refunded.")
else:
    if p_type == "y":
        if no_of_days <= 30:
            print("Refund available.")
        else:
            print("refund is not available for more than 30 days.")
    if p_type == "n":
        if no_of_days <= 30:
            print("total refund is available.")
        elif no_of_days <= 60:
            print("50% of the money can be refunded.")
        elif no_of_days <= 90:
            print("25% of the money can be refunded.")
        else:
            print("Refund time is completed. No refund available.")
    