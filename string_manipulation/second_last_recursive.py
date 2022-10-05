s=input('enter string')
new=""
rec=""
for i in s:
    if i not in new:
        new=new+i
    elif i not in rec:
        rec=rec+i
print("second last recursive is",rec[-2])