ticket_price = int(input("Enter the ticket price: "))
demand = int(input("Enter the demand percentage[80 - high || (40-80) - medium || (<40) - low]: "))
seat_type = input("Enter the seat type[VIP, regular]: ").lower()

if demand > 80:
    ticket_price = ticket_price * 1.2
elif demand < 40:
    ticket_price = ticket_price * 0.9

if seat_type == "vip":
    ticket_price += 50
print(f"Your final ticket price is {ticket_price}")