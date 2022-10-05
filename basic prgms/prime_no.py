# prime number
#2 prime
# 1,2

#3 prime
# 1,3

#4 not  prime
# 1,2,4

#5prime
# 1,5

#6   not prime
# 1,2,3,6

#7 prime
# 1,7

n=int(input("enter number to check"))
flag=0
for i in range(2,n):
    if n%i==0:
        flag=1
if flag==0:
    print("prime")
else:
    print("not prime")
#




