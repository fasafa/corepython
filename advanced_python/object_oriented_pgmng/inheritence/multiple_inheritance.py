class A:
    def printa(self):
        print("inside A")
class B:
    def printb(self):
        print('inside B')
class C(A,B):
    def printc(self):
        print('inside c')
c=C()
c.printc()
c.printa()
c.printb()