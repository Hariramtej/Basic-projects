credit_score = int(input("Enter your credit score: "))

if credit_score < 600:
    print("Your credit score is too low. Your loan is rejected")
elif credit_score >= 600:
    annual_income = int(input("Enter your annual income: "))
    existing_debt = int(input("Enter your debt value: "))
    if credit_score >= 600 and credit_score < 700:
        if annual_income > 50000 and existing_debt < 30000:
            print("You are approved for the loan.")
        else :
            print("You are not approved for th loan.")
    elif credit_score < 800:
        if annual_income > 40000 and existing_debt < 40000:
            print("You have be approved for the loan.")
        else:
            print("You are not approved for the loan.")
    else:
        print("You are approved for the loan.")