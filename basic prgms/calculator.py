def add(n1,n2):
    print(n1+n2)
def sub(n1,n2):
    print(n1-n2)
def mul(n1,n2):
    print(n1*n2)
def div(n1,n2):
    print(n1/n2)

while True:
    option=int(input('select option\n1.add\n2.sub\n3.mul\n4.div\n5.stop'))
    if option==5:
        break
    elif option in (1,2,3,4):
        num1=float(input("enter num1"))
        num2=float(input('enter num2'))
        if option==1:
            add(num1,num2)
        elif option==2:
            sub(num1,num2)
        elif option==3:
            mul(num1,num2)
        else:
            div(num1,num2)
    else:
        print('invalid option')


