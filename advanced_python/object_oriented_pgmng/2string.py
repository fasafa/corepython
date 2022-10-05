# to string
class Person:
    def setvalue(self,name,age,place):
        self.firstname=name
        self.age=age
        self.place=place
    def printvalue(self):
        print(self.firstname)
        print(self.age)
        print(self.place)
    def __str__(self):
        return self.firstname+self.place+str(self.age)
p1=Person()
p1.setvalue("safa",24,"kochi")
print(p1)
