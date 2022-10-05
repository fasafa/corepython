s=input('enter sting')
count={}
d=s.split(" ")
for i in d:
    if i not in count:
        count.update({i:1})
    else:
        val=count[i]
        val=val+1
        count.update({i:val})
print(count)
