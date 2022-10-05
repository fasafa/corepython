s=input('enter string')
new=""
rec=""
for i in s:
    if i not in new:
        new=new+i
    else:
        rec=rec+i
print("last recursive is",rec[-1])


