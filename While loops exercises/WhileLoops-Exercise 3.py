import random
def generate_numbers():
    return random.randint(1, 10), random.randint(1, 10)

while True:
    num1, num2 = generate_numbers()
    result = num1 + num2
    user_answer = int(input(f" What is the sum of {num1} and {num2}: "))
    if user_answer == result:
        print("Congrats, you got it right!!!!!!")
        break
    else:
        print("Wrong, try again!")