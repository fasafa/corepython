class Person:
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def printperson(self):
        print(self.name,self.age,self.place)
class Parent(Person):
    def __init__(self,phone_number,address,name,age,place):
        super().__init__(name,age,place)
        self.phone_number=phone_number
        self.address=address
    def printparent(self):
        print(self.phone_number,self.address)
class Empolyee(Parent):
    def __init__(self,id,des,salary,name,age,place,address,phone_number):
        super().__init__(address,phone_number,name,age,place)
        self.id=id
        self.des=des
        self.salary=salary
    def printemplyee(self):
        print(self.id,self.des,self.salary)
m=Empolyee(2,"dev",90000,"safa",67,"kochi","gdffdgdghsg",90765443)
m.printperson()
m.printparent()
m.printemplyee()

