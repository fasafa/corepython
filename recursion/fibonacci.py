def fib(n):
    if n<=1:
        return n
    else:
        return fib(n-1)+fib(n-2)
nterms=int(input("enter no terms"))
for i in range(nterms):
    print(fib(i))