l=[3,6,1,7,0,2,4]
newlist=[]
while l:
    minimum=l[0]
    for i in l:
        if i<minimum:
            minimum=i
    newlist.append(minimum)
    l.remove(minimum)
# print(newlist)
print('minimum element',newlist[0])
print('maximum value',newlist[-1])