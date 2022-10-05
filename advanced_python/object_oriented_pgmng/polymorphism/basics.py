# polymorphism
# 1.method overloading
# 2. method overriding
#  over loading === same name, diff number of arguments
class A:
    def printa(self,num1):
        self.num=num1
        print(self.num,'inside A')
class B(A):
    def printa(self,num1,num2):
        self.num1=num1
        self.num2=num2
        print(self.num1,self.num2,'inside b')
c=B()
c.printa(5)
c,print(5,8)
