normal_days = int(input("Enter no of days you were absent: "))
sick_days = int(input("Enter no of sick holidays: "))
bonus = 200

if 1 <= normal_days <= 3:
    bonus = 100
elif normal_days > 3:
    bonus = 0
if sick_days > 2:
    bonus = bonus * 0.5

print(f"Your attendence bonus is ${bonus}")