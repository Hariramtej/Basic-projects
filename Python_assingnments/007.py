age = int(input("Enter your age: "))

if age >= 18:
    citizenship = input("Are you the citizen of this country[y/n]: ")
    if citizenship == "y":
        voting_status = input("Have you voted before[y/n]: ")
        if voting_status == "y":
            print("You are eligible to vote.")
        else:
            print("You are eligible sice you already voted.")
    else:
        print("You are not eligible to vote since you are not the citizen of this country.")
else:
    print("You are not eligible for voting because you are under the age limit.") 