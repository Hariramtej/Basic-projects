user = input("Enter the user name: ")
password = input("Enter the password")

if user == "admin" and password == "12345":
    print("Login successful. Welcome!")
elif user != "admin":
    print("Username not found.")
elif password != "12345":
    print("Password is incorrect.")