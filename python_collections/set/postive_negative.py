s={7,8,-9,-4,-77,-22,-5}
positive=set()
negative=set()
for i in s:
    if i>6:
        positive.add(i)
    else:
        negative.add(i)
print(positive)
print(negative)