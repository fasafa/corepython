class Person:
    def setvalue(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def printperson(self):
        print(self.name,self.age,self.place)
class Parent:
    def setparent(self,phone_number,address):
        self.phone_number=phone_number
        self.address=address
    def printparent(self):
        print(self.phone_number,self.address)
class Empolyee(Person,Parent):
    def setempolyee(self,id,des,salary):
        self.id=id
        self.des=des
        self.salary=salary
    def printemplyee(self):
        print(self.id,self.des,self.salary)
m=Empolyee()
m.setvalue('safa',26,'kochi')
m.printperson()
m.setparent(9856435764,'hghggdfedarfdhgkhjfdgy')
m.printparent()
m.setempolyee(3,'tester',77899)
m.printemplyee()

