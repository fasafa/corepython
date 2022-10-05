class Student:
    college='rajigiri'
    def __init__(self,name,roll_no,department):
        self.name=name
        self.roll_no=roll_no

        self.department=department
    def printvalue(self):
        print("student name",self.name)
        print("roll no",self.roll_no)
        print("college name",Student.college)
        print("department name is",self.department)
name=input('enter name')
s=Student(name,4,'teacher')
s.printvalue()
print(s.name)
print(s.college)


