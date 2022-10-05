class Person:

    def setperson(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def printperson(self):
        print(self.name,self.age,self.place)
class Empolyee(Person):
    company_name = 'luminar'
    def setempolyee(self,id,salary):
        self.id=id
        self.salary=salary
    def printempolyee(self):
        print(self.name,self.age,self.place,self.id,self.salary,Empolyee.company_name)
e=Empolyee()
e.setperson('safa',23,'kochi')
e.setempolyee(2,4500)
e.printempolyee()