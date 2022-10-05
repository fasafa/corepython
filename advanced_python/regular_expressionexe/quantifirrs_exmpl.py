import re
count=0
x='a{2,4}'
matcher=re.finditer(x,'aaa aa aaa abc123ABC')
# print(matcher)
for i in matcher:
    print(i.start())
    print(i.group())
    count=count+1
print( "count =",count)