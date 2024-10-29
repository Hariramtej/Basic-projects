service = int(input("Enter the no of years of your service: "))
Leave_type = input("Why do you want a leave[vacation, sick, personal]: ")
no_of_days = int(input("Enter the number of days you want a leave: "))

if service < 1:
    if Leave_type == "sick":
        if no_of_days <= 5:
            print("Your leave is granted");
        else:
            print("You can only take 5 sick days for leave.")
    elif Leave_type == "vacation" or Leave_type == "personal":
        print("You cannot take any other leaves other than sick leaves.")
elif service <=3:
    if Leave_type == "sick":
        if no_of_days <=5:
            print("Leave is granted.")
        else:
            print("You can only take 5 sick leaves")
    elif Leave_type == "vacation":
        if no_of_days <= 5:
            print("Your leave is granted")
        else:
            print("You can only take 5 vacation days for leave.")
    elif Leave_type == "personal":
        print("You cannot take personal leaves.")
elif service <= 5:
    if Leave_type == "sick":
        if no_of_days <=10:
            print("Leave is granted.")
        else:
            print("You can only take 10 sick leaves")
    elif Leave_type == "vacation":
        if no_of_days <= 10:
            print("Your leave is granted")
        else:
            print("You can only take 10 vacation days for leave.")
    elif Leave_type == "personal":
        if no_of_days <=5:
            print("Leave is granted.")
        else:
            print("You can only take 5 personal leaves")
elif service > 5:
    if Leave_type == "sick":
            print("Leave is granted.")
    elif Leave_type == "vacation":
        if no_of_days <= 15:
            print("Your leave is granted")
        else:
            print("You can only take 15 vacation days for leave.")
    elif Leave_type == "personal":
        if no_of_days <=10:
            print("Leave is granted.")
        else:
            print("You can only take 10 personal leaves")