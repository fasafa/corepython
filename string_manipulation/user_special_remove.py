s="!@#$%^&*?"
u=input('enter string')
new=""
for i in u:
    if i not in s:
        new=new+i
print(new)
