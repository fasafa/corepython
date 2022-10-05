# functions without argument
def prime():
    n = int(input("enter number"))
    for i in range(2, n):
        if n % 2 == 0:
            print("not prime")
            break
    else:
        print("prime")
prime()
prime()
