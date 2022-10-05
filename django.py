s="ABBACC"
rec=""
for i in s:
    if i not in rec:
        rec=rec+i
    else:
        print(i)
        break