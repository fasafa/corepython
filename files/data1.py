f=open('data.txt','r')
f2=open('copydata.txt','w')
for i in f:
    f2.write(i)
    # d=i.rstrip('\n')
    # print(d)


