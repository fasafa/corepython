initial=int(input("enter initial range"))
final=int(input("enter final range"))
for num in range(initial,final+1):
    for i in range(2,num):
        if num%i==0:
            break
    else:
        print(num)


