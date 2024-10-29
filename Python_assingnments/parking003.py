violation_type = input("Enter the type of violation[no parking zone, loading zone,handicapped spot,over time limit]: ").lower()
fine = 0
if violation_type == "no parking zone":
    print("Your fine is $100.")
elif violation_type == "loading zone":
    print("Your fine is $75.")
elif violation_type == "handicapped spot":
    print("Your fine is $200.")
elif violation_type == "over time limit":
    no_of_hours = int(input("Enter the no of hours of violation: "))
    fine = no_of_hours * 50
    print(f"Your fine is {fine}")