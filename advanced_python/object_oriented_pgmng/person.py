class Person:
    def __init__(self,name,age,place):
        self.firstname=name
        self.age=age
        self.place=place
    def printvalue(self):
        print(self.firstname)
        print(self.age)
        print(self.place)
p1=Person(safa",24,"kochi)
# p1.setvalue("safa",24,"kochi")
p1.printvalue()

p2=Person()
p2.setvalue("sachu",67,"kollam")
p2.printvalue()

p3=Person()
p3.setvalue("susan",34,"kochi")
p3.printvalue()
