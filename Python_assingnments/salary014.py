rating = input("Enter your rating[Excellent, good, fair, poor]: ")
salary = int(input("Enter your salary: "))
years_of_service = int(input("Enter your years of service: "))
bonus = 0

if rating == "Excellent":
    bonus = salary * 0.2
elif rating == "good":
    bonus = salary * 0.1
elif rating == "fair":
    bonus = salary * 0.5

if years_of_service >= 10:
    bonus += 1000