initial=int(input("enter initial value"))
final=int(input("enter final value"))
sum=0
for i in range(initial,final+1):
    if i>0:
        sum=sum+i
print(sum)