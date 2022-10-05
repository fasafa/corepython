def factorial(n):
    fact=1
    while n>0:
        fact=fact*n
        n=n-1
    print("factorial of", "=",fact)
factorial(5)
factorial(6)
factorial(9)


n = int(input("enter number"))
def factorial(n):
    fact=1
    while n>0:
        fact=fact*n
        n=n-1
    print("factorial of", "=",fact)
factorial(n)
