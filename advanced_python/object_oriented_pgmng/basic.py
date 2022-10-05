# object oriented programming
# class -design pattern or blue print, methods and variables
# object   - real world entity
# reference- store ,to perform opertion

# laptop clss
# hp mac mi..... etc object
# student clss     even persons object

# self - instance variable

class Person:
    def walk(self):#instance variable
        print('person is walking')
    def read(self):
        print('person is reading')
p=Person()                               #p=reference   person()-object
p.read()
p.walk()

p2=Person()
p2.walk()
p2.read()