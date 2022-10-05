l=[5,8,9,2,3,4,7,6,1]
e=int(input('enter num'))      #8
l.sort()
flag=0                         # 0
low=0                           #0
upper=len(l)-1                  # 8
while low<=upper:
    mid=(low+upper)//2             #index    # 0+8//2=4
    if l[mid]==e:                    # l[4]=5
        flag=1
        break
    elif e>l[mid]:                     #8>5
        low=mid+1                      #4+1=5
    elif e<l[mid]:
        upper=mid-1
if flag==1:
    print('found')
else:
    print('not found')
