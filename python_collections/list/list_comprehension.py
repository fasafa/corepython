# s=[1,2,5,7,9,6]
# cube=[]
# for i in s:
#     cube.append(i**2)
# print(cube)

# # square list comprehension
# list=[1,2,5,7,9,6]
# square=[i**2 for i in list]
# print(square)

# l=[i for i in range(1,11)]
# print(l)

# # postive and negatiove
# l=[1,-3,5,-7,-1,4,7,9]
# positive=[i for i in l if i>0]
# negative=[i for i in l if i<0]
# print(positive)
# print(negative)

# 20 even numbers
even=[i for i in range(1,21) if i%2==0]
print(even)