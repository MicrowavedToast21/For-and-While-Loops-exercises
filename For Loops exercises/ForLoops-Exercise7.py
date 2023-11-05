n = int(input("Enter a positive integer: "))
def multiplicationTable(n):
    for i in range (1, 11):
        print("%d * %d = %d" % (n, i, n * i))
multiplicationTable(n)