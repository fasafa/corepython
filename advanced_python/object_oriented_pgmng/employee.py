class Employee:
    company_name='luminar'
    def setvalue(self,name,id,salary):
        self.name=name
        self.id=id
        self.salary=salary

    def printvalue(self):
        print("empolyee name is",self.name)
        print("empolyee id",self.id)
        print("empolyee salary",self.salary)
        print("empolyee company",Employee.company_name)
e=Employee()
e.setvalue("safa",1,4500)
e.printvalue()

e1=Employee()
e1.setvalue("ayma",2,20500)
e1.printvalue()

e2=Employee()
e2.setvalue("hizu",3,1000)
e2.printvalue()

