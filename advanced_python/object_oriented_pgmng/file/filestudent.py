class Student:
    def __init__(self,name,roll,mark):
        self.name=name
        self.roll=roll
        self.mark=mark
    def printstudent(self):
        print(self.name,self.roll,self.mark)
f= open("student")
for i in f:
    data=i.rstrip("\n").split(",")
    name=data[0]
    roll=data[1]
    mark=data[2]
    st=Student(name,roll,mark)
    st.printstudent()
    print(st.mark)
    print(st.name)