s={1,5,7,9,2,4,6,8}
odd=set()
even=set()
for i in s:
    if i%2==0:
        even.add(i)
    else:
        odd.add(i)
print(even)
print(odd)
