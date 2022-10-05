class Person:
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def printperson(self):
        print(self.name,self.age,self.place)
class Parent:
    def __init__(self,phone_number,address):
        self.phone_number=phone_number
        self.address=address
    def printparent(self):
        print(self.phone_number,self.address)
class Empolyee(Person,Parent):
    def __init__(self,id,des,salary,name,age,place,phone_number,address):
        Person.__init__(self,name,age,place)
        Parent.__init__(self,phone_number,address)
        self.id=id
        self.des=des
        self.salary=salary
    def printemplyee(self):
        print(self.id,self.des,self.salary,self.age,self.name)
m=Empolyee(1,"dev",90000,"safa",45,"kochi",9876544323,"kkkkkkkkkaaa")
m.printemplyee()
m.printparent()

