class Person:
    def setvalue(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def printvalue(self):
        print(self.name,self.age,self.place)
class Student(Person):
    def setstudent(self,roll_no,department,school):
        self.roll_no=roll_no
        self.department=department
        self.school=school
    def printstudent(self):
        print(self.name,self.age,self.place,self.roll_no,self.department,self.school)
s=Student()
s.setstudent(3,'cse','luminar')
s.setvalue('safa',37,'kochi')
s.printstudent()
print(s.age)
