while True:
    user = input("Are you done? (yes/no): ").lower()
    if user == "yes":
        print("Okay you're done!")
        break
    elif user == "no":
        print("Tell me when you're done!")
    else:
        print("Invalid input. Please enter y or n!")
