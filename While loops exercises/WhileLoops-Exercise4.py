password = "CompSci23"
while True:
    user_answer = (input("Enter the password:"))
    if user_answer == password:
        print("Congrats you got the password right!")
        break
    else:
        print("Wrong password! Try again!")
