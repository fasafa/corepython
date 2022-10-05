
stack=[]
size=int(input('enter the size'))
top=0
def push():
    global top,size
    if top>=size:
        print("stack is full")
    else:
        e=int(input("enter elemets to add"))
        stack.append(e)
        top=top+1
        print(stack)
def pop():
    global top,size
    if top<=0:
        print('stack is empty')
    else:
        stack.pop()
        top=top-1
        print(stack)
while True:
    option=int(input('enter operation\n1.push\n2.pop\n'))
    if option==1:
        push()
    else:
        pop()

