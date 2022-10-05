# def sub(n1,n2):
#     return  n1-n2
# print(sub(2,1))
# print(sub(5,9))

def changevalu(func):
    def wrapper(a,b):
        if a>b:
            return func(a,b)
        else:
            a,b=b,a
            return func(a,b)
    return wrapper
@changevalu
def sub(n1,n2):
    return  n1-n2
# print(sub(5,9))
@changevalu
def div(n1,n2):
    return n1/n2
print(div(3,6))