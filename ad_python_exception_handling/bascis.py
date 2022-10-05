# # exception handling
# n=int(input('enter num'))
# n2=int(input('enter num'))
# print(n/n2)
# try
n=int(input('enter num'))
n2=int(input('enter num'))
try:
    print(n/n2)
except Exception as a:
    print(a)
finally:
    print('in finally')