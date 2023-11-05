n = int(input("Enter a number of rows: "))
def print_diamond(n):#creates function for diamond
    for i in range(n):
        print(" " * (n - i - 1) + "#" * (2 * i + 1))#prints upper part
    for i in range(n - 2, -1, -1):
        print(" " * (n - i - 1) + "#" * (2 * i + 1))#prints bottom part

print_diamond(n)#prints complete diamond