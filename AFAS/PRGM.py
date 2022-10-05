# fixed_am =1000
# withdraw =int(input('enter amount'))
# if withdraw>fixed_am:
#     print('insufficient balance',withdraw)
# else:
#     print('your balance is',fixed_am)
# print("total balance is",fixed_am-withdraw)


# fibonacci 0 1 1 2 3 5 8.....

# n1=0
# n2=1
# for i in range(10):
#     print(n1)
#     nth=n1+n2
#     n1=n2
#     n2=nth

# # swapping method tuple
# n1=10
# n2=5
# n1,n2=n2,n1
# print(n1,n2)

# # positive negative
# def number():
#     n=int(input('enter number'))
#     if n>0:
#          print('positive')
#     elif n==0:
#         print('zero')
#     else:
#         print('negative')
# number()
# function with argument return type
# def even_and_odd_check(n):
#     if n%2==0:
#         return 'even'
#     else:
#         return 'odd'
# print(even_and_odd_check(9))
# print(even_and_odd_check(6))

# to find greatest number
# def grts(n1,n2):
#     if n1>n2:
#         return 'n1 is greater'
#     elif n2>n1:
#         return 'n2 is greater'
#     else:
#         return 'equel'
# print(grts(100,600))
# print(grts(10,600))

# # 100 below
# 90-100 a+
# 80-89 a
# 70-79 b+
# 60-69 b
# 50-59 c
# 50 below fail
# 101 invalid
# def mark():
#     n=int(input("enter mark"))
#     if n<=100:
#         if n>=90:
#             print('A+')
#         elif n>=80:
#             print("A")
#         elif n>=70:
#             print('B+')
#         elif n>=60:
#             print('B')
#         elif n>=50:
#             print("c")
#         elif n<=50:
#              print("fail")
#     else:
#         print('invalid mark')
# mark()

# number idayil ulla even number print
# initial=int(input("enter initial number"))
# final=int(input('enter final number'))
# for i in range(initial,final+1):
#     if i%2==0:
#         print(i)
#  square val

# initial=int(input("enter initial"))
# final=int(input('enter final'))
# for i in range(initial,final+1):
#     print(i**2)

# multiplication

# factorial
# n=int(input('enter number'))
# fact=1
# for i in range(1,n+1):
#     fact=fact*i
# print(fact)

# # odd user
# initial=int(input("enter initial number"))
# final=int(input('enter final number'))
# for i in range(initial,final+1):
#     if i%2!=0:
#         print(i)
# even sum
# initial=int(input("enter initial number"))
# final=int(input('enter final number'))
# sum=0
# for i in range(initial,final+1):
#     if i%2==0:
#         sum=sum+i

# print(sum)rs
# # postive numbes sum
# initial=int(input("enter initial number"))
# final=int(input('enter final number'))
# sum=0
# for i in range(initial,final):
#     if i>0:
#         sum=sum+i
# print(sum)

#  square val
# initial = int(input("enter initial"))
# final=int(input('enter final'))
# sum=0
# for i in range(initial,final+1):
#     if i**2:
#         sum=sum+i
# print(sum)

# WHILE LOOP multiplication
# n=int(input('enter number'))
# i=1
# while i<=10:
#     print(i,"*",n,"=",i*n)
#     i+=1

# hacker rank 2nd prblm
# n=int(input("enter number"))
# if n%2!=0 or (n>=6 and n>=20):
#     print('Weird')
# else:
#     print("not Weird")

# n=int(input("enter number "))
# n2=int(input("enter number"))
# while n<=n2:
#     if n%2==0:
#         print(n)
#     n+=1

# initial=int(input('enter number'))
# final=int(input('enter final'))
# sum=0
# for i in range(initial,final+1):
#     if i%2==0:
#         sum=sum+i
# print(sum)


# initial=int(input('enter number'))
# final=int(input('enter final'))
# sum=0
# while initial<final:
#     if initial%2==0:
#         sum=sum+initial
#     initial=initial+1
# print(sum)

# n=int(input("enter number"))
# fact=1
# for i in range(1,n+1):
#     fact=fact*i
# print(fact)

# n=int(input("enter numbver"))
# fact=1
# while n>0:
#     fact=fact*n
#     n=n-1
# print(fact)


# n=int(input("enter numbver"))
# i=1
# while i<=10:
#     print(i*n)
#     i+=1
#

# fibonnoci
# 0,1,1,2,3,5,8....
# n1=0
# n2=1
# for i in range(11):
#     print(n1)
#     nth=n1+n2
#     n1=n2
#     n2=nth

# prime
# n=int(input("enter number"))
# for i in range(2,n):
#     if n%i==0:
#         print("not prime")
#         break
# else:
#     print('prime')
# prime sum

# initial=int(input('enter initial number'))
# final=int(input("enete final number"))
# sum=0
# for num in range(initial,final+1):
#     for i in range(2,num):
#         if num%i==0:
#             break
#     else:
#         sum=sum+num
# print(sum)

# # user input prime range
# initial=int(input('enter initial number'))
# final=int(input("enete final number"))
# for num in range(initial,final+1):
#     for i in range(2,num):
#         if num%i==0:
#             break
#     else:
#         print(num)
# string manupulatiom
# collection of elements


# # present and not present
# def check():
#     s='ayman hadee hizu'
#     e=input('emter string to check')
#     for i in s:
#         if i==e:
#             print('present')
#             break
#         else:
#             print('not pressent')
# check()
# check()
#

# method 2
# s='safasafasaasaaaaammm'
# e=input('enter chck')
# if e in s:
#     print('present')
# else:
#     print('not presnet')
#
# # method3
# s='asdfghjkl'
# e=input('enter string to chec')
# if e not in s:
#     print("not present")
# else:
#     print('present')

# common elements
# s1='abcd'
# s2='aczy'
# for i in s1:
#     if i in s2:
#         print(i)
# user input count
# s='aaabbccddee'
# user=input('enter dighit')
# count=0
# for i in s:
#     if i in user:
#         count=count+1
# print(count)

# vowels count
# s=input("enter string")
# v='aeiou'
# count=0
# for i in v:
#     if i in s:
#         count=count+1
# print(count)

# s=input("enter string")
# count=0
# for i in s:
#     if i in 'aeioue':
#         count=count+1
# print(count)

# s='abcd'
# s2=''
# for i in s:
#     s2=s2+i
# # print(s2)
# s=input('enter string')
# s2=''
# for i in s:
#     s2=s2+i
# print(s2)
# first recursive element
# s=input('enter string')
# e=''
# for i in s:
#     if i not in e:
#         e=e+i
#     else:
#         print(i)

# second recursive element
# s=input('ente string')
# new=""
# rec=""
# for i in s:
#     if i not in new:
#         new=new+i
#     elif i not in rec:
#         rec=rec+i
#     else:
#         print(rec[1])
#         b
# to remove userin put letter
# s='safahizu'
# v=input('enete rmove number')
# new=''
# for i in s:
#     if i not in v:
#         new=new+i
# print(new)

# s="!@#$%^&*(()"
# v=input('enter remove')
# new=''
# for i in v:
#     if i not in s:
#         new=new+
# prinlst=
# Students =[('anu',67),('amal',69),('arun',65)]
# newlist=[]
# while Students:
#     maximum=Students[0]
#     for i in Students:
#         if i>maximum:
#             maximum=i
#     newlist.append(maximum)
#     Students.remove(maximum)
# print('maximum element',newlist[-1])
#
# b=[3,77,0,5,33,6,22,5,90,32,56,78,98,54,67,11,34,88]
# e=[b.remove(mid_index=(len(b)-1)//2)]
# mid_index=(len(b)-1)//2
# mid_index=e
# b.remove()
# print(b[mid_index])
# create a function with arguments and return type which find sum of odd numbers between 40 -8def add(num1,num2):
# s=6
# for i in range(5):
#     for a in range(s):
#         print(end=" ")
# #     s=s-1
# #     for j in range(i):
#         print("*",end=" ")
#     print()
# s=1
# for i in range(5,0,-1):
#     for a in range(s):
#         print(end=" ")
#     s=s+1
#     for j in range(i):
#         print("*",end=" ")
#     # print()
# s=1
# for i in range(5,0,-1):
#     for j in range(i):
#         print('*',end=" ")
#         s = s - 1
#     print()
# def add(n1, n2):
#     print(n1 + n2)
# def sub(n1, n2):
#     print(n1 - n2)
# def mul(n1, n2):
#     print(n1 * n2)
# def div(n1, n2):
#     print(n1 / n2)
# def floordiv(n1,n2):
#     print(n1//n2)
# def exponent(n1,n2):
#     print(n1**n2)
# while True:
#     option = int(input('select option\n1.add\n2.sub\n3.mul\n4.div\n5.floordiv\n6.exponent'))
#     if option == 7:
#         break
#     elif option in (1,2,3,4,5,6):
#         num1 = float(input("enter num1"))
#         num2 = float(input('enter num2'))
#         if option == 1:
#             add(num1, num2)
#         elif option == 2:
#             sub(num1, num2)
#         elif option == 3:
#             mul(num1, num2)
#         elif option == 4:
#             floordiv(num1, num2)
#         elif option == 5:
#             exponent(num1, num2)
#         else:
#             div(num1, num2)
#     else:
#         print('invalid option')

# Function to demonstrate printing pattern

#  star l back
# s = 6
# for i in range(1,s):
#     # num = 1
#     for j in range(s, 0, -1):
#         if j > i:
#             print(" ", end=' ')
#         else:
#             print('*', end=' ')
#
#     print("")
# n=4
# n2=3
# num=n+n2
# print(n+n2%5)
# user factorial
# n = int(input("enter number"))
# def factorial(n):
#     fact=1
#     while n>0:
#         fact=fact*n
#         n=n-1
#     print("factorial of", "=",fact)
# factorial(n)

# create a function to find sum of odd numbers from 20 to 30?
# initial=int(input("enter number"))
# final=int(input("enter number2"))
# sum=0
# def odd():
#     global sum
#     for i in range(20,30):
#         if i%2!=0:
#             sum=sum+i
#             print(sum)
# odd()
#
# 2.create a function with argument and return type to find grade of student?

# code to find sum of +ve numbers between -5 to 10 using function with argument?
# sum=0
# def positive(initial,final):
#     global sum
#     for i in range(initial,final):
#         if i>0:
#             sum=sum+i
# print(positive(-5,11),sum)

# 2.create a function with argument and return type to find grade of student?
#
# def student(grade):
#     if grade<=100:
#         if grade>=90:
#             return "A+"
#         elif grade>=80:
#             return  'A'
#         elif grade>=70:
#              return "B+"
#         elif grade>=60:
#             return "B"
#         elif grade>=50:
#              return "c"
#         elif grade<50:
#             return "fail"
#     else:
#         return "invalid number"
# print(student(90))
# print(student(80))
# print(student(75))
# print(student(60))
# print(student(50))
# print(student(45))
# print(student(110))


# advnced python
# class Colleage:
#     college="luminar"
#     def setvalue(self,department,course,teachers):
#         self.department=department
#         self.course=course
#         self.teachers=teachers
#     def printvalue(self):
#         print(self.department,self.course,self.teachers,Colleage.college)
# cc=Colleage()
# cc.setvalue("cse","manga","sachu")
# cc.printvalue()
# cc.college
# class Empolyee:
#     company_name="luminar"
#     def __init__(self,name,id,age,place):
#         self.name=name
#         self.id=id
#         self.age=age
#         self.place=place
#     def printemlyee(self):
#         print(self.name,self.age,self.id,self.place,Empolyee.company_name)
# em=Empolyee("safa",2,22,"kochi")
# # em.setvalue("safa",2,22,"kochi")
# em.printemlyee()

# em1=Empolyee()

# em1.setvalue("sachu",3,34,"kochi")
# em1.printemlyee()
#
# print(em.name)

# single inheritance
# class A:
#     college="luminar"
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def printa(self):
#         print(self.name,self.age)
# class B(A):
#     def __init__(self,plce,department,name,age):
#         super().__init__(name,age)
#         self.place=plce
#         self.department=department
#
#     def printb(self):
#         print(self.name,self.age,self.place,self.department,A.college)
# ab=B("safa",22,"kochi","eee")
# # ab.setvalue("safa",22)
# # ab.setvalueb("kochi","cptr")
# ab.printb()

# multiple inheritence

# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def printperson(self):
#         print(self.name,self.age)
# class Student:
#     def __init__(self,place,id):
#         self.place=place
#         self.id=id
#     def printstudent(self):
#         print(self.id,self.place)
# class Employee(Person,Student):
#     compny="luminar"
#     def __init__(self,salary,name,age,place,id):
#         Person.__init__(name,age)
#         Student.__init__(place,id)
#         self.salary=salary
#         # self.company=company
#     def printemplyee(self):
#         print(self.name,self.age,self.id,self.place,self.salary,Employee.compny)
# em=Employee("safa",88,"kochi",7,89000)
# # em.setstudent("kochi",3)
# # em.setperson("safa",22)
# # em.emvalue(30000)
# em.printemplyee()
#
# # hierachiel/multilevel inheritence
# # class Person:
# #     def setvalue(self,name,age,place):
# #         self.name=name
# #         self.age=age
# #         self.place=place
# #     def printperson(self):
# #         print(self.name,self.age,self.place)
# # class Parent(Person):
# #     def setparent(self,phone_number,address):
# #         self.phone_number=phone_number
# #         self.address=address
# #     def printparent(self):
# #         print(self.phone_number,self.address,self.name,self.age,self.place)
# # class Empolyee(Parent):
# #     def setempolyee(self,id,des,salary):
# #         self.id=id
# #         self.des=des
# #         self.salary=salary
# #     def printemplyee(self):
#         print(self.id,self.des,self.salary)
# m=Empolyee()
# m.setvalue('safa',26,'kochi')
# m.setparent(90876544322,"kkkjjghdfs")
# m.printparent()

# anagram
# string1=input("enter string here")
# string2=input("enter string 2 here")
# s1=sorted(string1)
# s2=sorted(string2)
# if s1==s2:
#     print("true")
# else:
#     print("false")


# s=input("enter string")
# m=s.split(" ")
# a=""
# for i in m:
#     i
# print(m)


# fibonnoci
# n1=0
# n2=1
# for i in range(10):
#     print(n1)
#     nth=n1+n2
#     n1=n2
#     n2=nth

# swapping number
# n1=int(input("enter number"))
# n2=int(input("enter number 2"))
# tem=n1
# n1=n2
# n2=tem
# print(n1)
# print(n2)
# prime
# n=int(input("enter number"))
# for i in range(2,n):
#     if n%i==0:
#         print("not prime")
#         break
#     else:
#         print("prime")

# reverse number
# n=int(input("enter number"))
# print(str(n)[::-1])
# text="hello hai hello hai"

# factorial


# def fact(n):
#     if n==1:
#         return n
#     else:
#         return n*fact(n-1)
# print(fact(5))

# def factorial(num):
#     fact=1
#     for i in range(1,num+1):
#         fact=fact*i
#     return fact
# print(factorial(5))
#
# s=input("enter strimg")
# if s==s[::-1]:
#     print("palindrome")
# else:
#     print("not palindrome")

# s="safapssafa"
# index=int(input("enter index"))
# print(s[index])

# s=input("enter string")
# mid_index=(len(s)-1)//2
# print(s[mid_index])

# remove s
# s="safasafasafasa"
# a=input("enter remove element")
# new=""
# for i in s:
#     if i not in a:
#         new=new+i
# print(new)

# remove vowels
# s="aeiou"
# m=input("enter string")
# new=""
# for i in m:
#     if i not in s:
#         new+=i
# print(new)

# # factori 1*2*3*4*5=120
# n=int(input("enter number to check factorial"))
# fact=1
# for i in range(1,n+1):
#     fact=fact*n
#     n=n-1
# print(fact)

# fibonocci 0 1 1 2 3 5 8 13....
# n1=0
# n2=1
# for i in range(10):
#     print(n1)
#     nth=n1+n2
#     n1=n2
#     n2=nth


# prime number fst 1 or same number divide cheyn pattnam
# n=int(input("enter number"))
# flag=0
# for i in range(2,n):
#     if n%i==0:
#         flag = 1
# if flag==0:
#     print("prime")
# else:
#     print("not prime")

# sum of prime numbe
# initial=int(input("enter numnber"))
# final=int(input("enter final number"))
# sum=0
# for num in range(initial,final+1):
#     for i in range(2,num):
#         if num%i==0:
#             break
#     else:
#         sum=sum+num
# print(sum)

# prime number range
# initial=int(input("enter numnber"))
# final=int(input("enter final number"))
# for num in range(initial,final+1):
#     for i in range(2,num):
#         if num%i==0:
#             break
#     else:
#         print(num)


# # factorial
# n=int(input("enter num"))
# fact=1
# for i in range(1,n+1):
#     fact=fact*n
#     n=n-1
# print(fact)

# remove vowel
# v="aeiou"
# s=input("enter string")
# new=""
# for i in s:
#     if i not in v:
#         new=new+i
# print(new)

# data operators

# print(True<=False)

# s=input("enter string")
# if s==s[::-1]:
#     print("palindrome")
# else:
#     print("not palindrome")

# s="safa"
# print(s[::-1])

# x,y,z="ornge","banaba","apple"
# print(x)
# print(y)
# print(z)

# unpacking
# fruits=["apple","orange","grapes"]
# x,y,z=fruits
# print(x)
# print(y)
# print(z)

# x = "Python"
# y = "is"
# z = "awesome"
# print(x,y,z)

# x = 5
# y = "John"
# print(x + y) error

# x = 5
# y = "John"
# print(x, y)
# x = "awesome"
#
# def myfunc():
#   print("Python is " + x)
#
# myfunc()

# x = "awesome"
#
# def myfunc():
#   x = "fantastic"
#   print("Python is " + x)
#
# myfunc()
#
# print("Python is " + x)

# x = "awesome"
# def myfunc():
#   global x
#   x = "fantastic"
# myfunc()
# print("Python is " + x)
# string roatation
# s=input("enter string")
# print(s[-2:]+s[:-2])

# s="luminar technolab"
# index=int(input("enter indeex"))
# print(s[index])
#
# s=input("enter string")
# mid_index=(len(s)-1)//2
# print(s[mid_index])

# a="bcd"
# h=""
# for i in a:
#     h=h+i
# print(h)

# remove vowels in this list
# s=input("enter string")
# v="aeiou"
# new=""
# for i in s:
#     if i not in v:
#         new=new+i
# print(new)


# count
# s=input("enter string")
# count=0
# v="aeiou"
# for i in s:
#     if i in v:
#         count+=1
# print(count)













