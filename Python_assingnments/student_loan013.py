age = int(input("Enter your age: "))
annual_income = int(input("Enter your annual income: "))
loan_amount = int(input("Enter the required loan amount: "))
repayment = 0

if annual_income < 40000:
    repayment = loan_amount * 0.1
elif annual_income < 80000:
    repayment = loan_amount * 0.08
elif annual_income >= 80000:
    repayment = loan_amount * 0.05

if age < 25:
    repayment -= repayment * 0.05

print(f"Your monthly repayment is ${repayment}")