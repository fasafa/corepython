def positive_negative(n):
    if n>0:
        return "postive"
    elif n==0:
        return "zero"
    else:
        return "negative"
print(positive_negative(-9))
print(positive_negative(0))
print(positive_negative(9))