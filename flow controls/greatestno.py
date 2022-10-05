# n1=int(input('enter numbern1'))
# n2=int(input('enter number2'))
# n3=int(input("enter numbr 3"))
# if n1>n2:
#     print("n1 is greater")
# elif  n2>n1:
#     print("n2 is greater" )
# elif n3<n2:
#     print("n3 is gra")
#
# else:
#     print("equel")

# heights = [100, 2, 300, 10, 11, 1000]
# largest_number = heights[0]
# for number in heights:
#     if number > largest_number:
#         largest_number = number
# print(largest_number)

a = int(input('Enter first number : '))
b = int(input('Enter second number : '))
c = int(input('Enter third number : '))
largest = 0
if a > b and a > c :
    largest = a
elif b > c :
        largest = b
else :
        largest = c
print(largest, "is the largest of three numbers.")