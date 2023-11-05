import math
user_integer = int(input("Enter the last integer: "))
x=0
for i in range(x, user_integer + 1):
    x+=i
print(f"The sum of all numbers from 1 to {user_integer} is:",x)