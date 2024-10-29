temp = int(input("Enter the temperature: "))

if temp < 0:
    print("Wear a heave coat. It's freezing outside!")
elif 0 <= temp <= 15:
    print("Wear a jacket. It's a bit chilly.")
elif 16 <= temp <= 25:
    print("Wear a sweater or long sleeves. It's a bit hot outside.")
else:
    print("Wear short and t-shirt. It's really hot outside.")