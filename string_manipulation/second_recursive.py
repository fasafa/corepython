s=input('enter string')
new=""
rec=""
for i in s:
    if i not in new:
        new=new+i
    elif i not in rec:
        rec=rec+i
print("second recursive is",rec[1])
