s=input("enter string")
e=""
for i in s:
    if i not in e:
        e=e+i
    else:
        print("first recursive element",i)
        break