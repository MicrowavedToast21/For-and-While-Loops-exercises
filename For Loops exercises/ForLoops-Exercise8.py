def factorial(n):
    res = 1
    for i in range(2, n+1):
        res *= i
    return res

n = int(input('Enter a positive integer: '))
print("factorial of", n,"is ", factorial(n))