# QUESTION - 1 ✅

# traveler_age = input("Enter your age catogary [Childern,Senior,Others]: ").lower()
# travelling_class = input("Enter the class you want to travel[Economy, Business, First]: ").lower()
# ticket_price = int(input("Enter the base ticket price: "))

# if travelling_class == "economy":
#     if traveler_age == "childern":
#         ticket_price -= ticket_price*0.3
#     elif traveler_age == "senior":
#         ticket_price -= ticket_price*0.2
# elif travelling_class == "business":
#     if traveler_age == "childern":
#         ticket_price -= ticket_price*0.4
#     elif traveler_age == "senior":
#         ticket_price -= ticket_price*0.25
# elif travelling_class == "first":
#     if traveler_age == "childern":
#         ticket_price -= ticket_price*0.5
#     elif traveler_age == "senior":
#         ticket_price -= ticket_price*0.3

# print(f"Your final ticket price is ${ticket_price}")

# QUESTION - 2 ✅

# product_type = input("Enter the product type[Limited edition, clearance sale, others]: ").lower()
# product_damage = input("Is the product damaged[Yes/ No]: ").lower()
# return_days = int(input("Return days: "))

# if product_damage == "no":
#     if product_type == "limited edition" or product_type == "clearance sale":
#         if return_days <= 30 :
#             print("Full refund. Product is not  damaged")
#         elif return_days > 30:
#             print("Refund is valid only for 30 days.")
#     else:
#         if return_days <= 30 :
#             print("Full refund avilable")
#         elif return_days <= 60:
#             print("50% of the money is returned")
#         elif return_days <= 90:
#             print("25% of the money is reunded")
#         elif return_days > 90:
#             print("Refundable date is completed. Cannot refund now")

# elif product_damage == "yes":
#     if return_days <= 90:
#         print("All the money can be refunded. Product is damaged")
#     elif return_days > 90:
#             print("Refundable date is completed. Cannot refund now")    

# QUESTION - 3 ✅

# violation_type = input("""Enter the type of vilation[no parking zone, loading zone, handicapped spot, over the time limit]: """).lower()

# fine = 0

# if violation_type == "no parking zone":
#     fine = 100
#     str = "You parked in no parking zone"
# elif violation_type == "loading zone":
#     fine = 75
#     str = "You parked in loading zone"
# elif violation_type == "handicapped  spot":
#     fine = 200
#     str = "You parked in handicapped spot"
# elif violation_type == "over the time limit":
#     time_over_limit = int(input("Enter the number of hours of overlimit: "))
#     str = "You parked over the time limit"
#     fine = 50 * time_over_limit

# print(f"Your fine is {fine}. {str}")

# QUESTION - 4 ✅

# age = int(input("Enter your age: "))
# event_type = input("Enter the event you wnat to participate in[concert, workshop, conference, other]: ").lower()

# if event_type == "concert":
#     if age >= 18:
#         print("You are now registered for this event")
#     else:
#         print("You cannot register to this event. You should be above 18 years.")
# elif event_type == "workshop":
#     if age >= 21:
#         print("Your age now registered for the above event.")
#     else:
#         print("You cannot register for this event.You should be above 21 years old.")
# elif event_type == "conference":
#     membership = input("Do you have membership status?[Y/N] ").lower()
#     if membership == "y":
#         print("You are now registered for this even.")
#     else:
#         print("You cannot register. This event requires membership to participate.")

# QUESTION - 5 ✅

# service = int(input("Enter number of years of your service: "))
# leave_type = input("Enter the type of leave you are requesting for[sick, vacation, personal]: ").lower()
# no_of_leaves = int(input("Enter number of days you want leave: "))
# if service < 1:
#     if leave_type == "sick":
#         if no_of_leaves <= 5:
#             print("You are granted for leaves")
#         else:
#             print("You can only take 5 sick leaves.")
#     else:
#         print("You can only take 5 sick leaves.")
# elif service <= 3:
#     if leave_type == "sick":
#         if no_of_leaves <= 5:
#             print("You are granted for leaves")
#         else:
#             print("You can only take 5 sick leaves.")
#     elif leave_type == "vacation":
#         if no_of_leaves:
#             print("You are granted leave.")
#         else:
#             print("You can only take 5 vacation leaves")
#     else:
#         print("You can only take sick or vatation leaves.")
# elif service <= 5:
#     if leave_type == "sick":
#         if no_of_leaves <= 10:
#             print("You are granted to take leave.")
#         else:
#             print("You can only take 10 sick leaves.")
#     elif leave_type == "vacation":
#         if no_of_leaves <= 10:
#             print("You are granted to take leave.")
#         else:
#             print("You can only take 10 vacation leaves.")
#     elif leave_type == "personal":
#         if no_of_leaves <= 5:
#             print("You are granted to take leave.")
#         else:
#             print("You can only take 5 personal leaves.")
# else:
#     if leave_type == "sick":
#         print("Your leave is granted.")
#     if leave_type == "vacation":
#         if no_of_leaves <= 15:
#             print("Your leave is granted")
#         else:
#             print("You can only take 15 vacation leaves.")
#     elif leave_type == "personal":
#         if no_of_leaves <= 10:
#             print("Your leave is granted.")
#         else:
#             print("You can only take 10 personal leaves.")




