#greatest among two number
def greatestnum(n1,n2):
    if n1>n2:
        return "n1 is greater"
    elif n2>n1:
        return "n2 is greater"
    else:
        return "equal"
print(greatestnum(100,200))