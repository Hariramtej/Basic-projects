age = int(input("Enter your age: "))
event_type = input("Enter the event type[Concert, workshop,conference]")

if event_type == "concert":
    if age >= 18:
                print("You are now registered for the concert.")
    else:
        print("You are below 18. You cannot register for the concert.")
elif event_type == "workshop":
    if age >= 21:
        print("You are now registered for the workshop")
    else:
        print("You cannot register since your age is lesser than 21")
elif event_type == "conference":
    membership = input("Do you have any memnership[y/n]: ")
    if membership == "y":
        print("You are now registered for the conference")
    else:
        print("You cannot register since you don't have a membership")
    
        