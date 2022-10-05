queue=[]
size=int(input('enter the size'))
top=0
def enqueue():
    global top,size
    if top>=size:
        print("queue is full")
    else:
        e=int(input("enter elemets to add"))
        queue.push(e)
        top=top+1
        print(queue)
def dequeue():
    global top,size
    if top<=0:
        print('queue is empty')
    else:
        queue.remove(queue([0]))
        top=top-1
        print(queue)
while True:
    option=int(input('enter operation\n1.enqueue\n2.dequeue\n'))
    if option==1:
        enqueue()
    else:
        dequeue()

