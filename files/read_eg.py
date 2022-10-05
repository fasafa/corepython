f=open('example.txt','r')
for i in f:
    data=i.rstrip('\n')
    print(data)
    # print(i)
