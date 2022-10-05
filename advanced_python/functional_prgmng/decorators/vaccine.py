def agecheck(f):
    def wrapper(a,b):
        if b<18:
            raise Exception("not elgible")
        else:
            return f(a,b)
    return wrapper

@agecheck
def vaccine(name,age):
    return "vaccinated successfully"
# print(vaccine("safa",21))
print(vaccine("safa",12))