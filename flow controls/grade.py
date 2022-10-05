name=input("enter your name")
grade=int(input("enter your mark"))
if grade<=100:
    if grade>=90:
        print("A+")
    elif grade>=80:
        print("A")
    elif grade>=70:
        print("B+")
    elif grade>=60:
        print("B")
    elif grade>=50:
        print("c")
    elif grade<50:
        print("fail")
else:
    print("invalid number")
