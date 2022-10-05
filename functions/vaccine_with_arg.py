def eligible_check(name,age):
    if age>=18:
        print(name,"your elgible")
    else:
        print(name,"your not elgible")
name=input("enter name")
age=int(input("enter age"))
eligible_check(name,age)
name1=input("enter name")
age1=int(input("enter age"))
eligible_check(name1,age1)

# eligible_check("safa",13)
# eligible_check(safa,18)
