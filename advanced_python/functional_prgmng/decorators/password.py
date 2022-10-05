def userpasscheck(f):
    def wrapper(a,b):
        if a=="admin":
            return f(a, b)
        else:
            raise Exception('user not admin')
    return wrapper
@userpasscheck
def changepassword(username,newpassword):
    mypassword=newpassword
    return mypassword
# print(changepassword("admin",6788))
print(changepassword("user",6788))