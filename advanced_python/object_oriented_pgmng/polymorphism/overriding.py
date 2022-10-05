# over riding
# same method names and same number of arguments
# child class method over rides parent class method
class A:
    def printa(self, num1):
        self.num = num1
        print(self.num, 'inside A')


class B(A):
    def printa(self,no1):
        self.no1 = no1
        print(self.no1,'inside b')


c = B()
c.printa(5)
