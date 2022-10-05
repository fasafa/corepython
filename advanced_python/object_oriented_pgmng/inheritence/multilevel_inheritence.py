# hierachical
class A:
    def printa(self):
        print('inside A')
class B(A):
    def printb(self):
        print('inside b')
class C(B):
    def printc(self):
        print('inside c')
m=C()
m.printc()
m.printb()
m.printa()