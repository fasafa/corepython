class Person:
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def printvalue(self):
        print(self.name,self.age,self.place)
class Student(Person):
    def __init__(self,roll_no,department,school,name,age,place):
        super().__init__(name,age,place)
        self.roll_no=roll_no
        self.department=department
        self.school=school
    def printstudent(self):
        print(self.name,self.age,self.place,self.roll_no,self.department,self.school)
s=Student(3,"eee","abcd","luminar","safa",33)
s.printstudent()

