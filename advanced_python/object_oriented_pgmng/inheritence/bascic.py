class A:
    def printa(self):
        print('inside A class')
class B(A):
    def printb(self):
        print('inside B class')
b=B()
b.printb()
b.printa()