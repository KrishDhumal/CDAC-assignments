"""sum = 0
for i in range(5):
    sum += i
print(sum)
for i in range(1,10):
    print(i)"""
#from idlelib.debugobj import dispatch

"""expense_list=[1230,2240,1500,1678,2020,1580,2240,1450,'1500',1245,2300]
total_expense=0

for expense in expense_list:
    total_expense+=expense

print("total expense is \t",total_expense)
"""
"""myset={x for x in range(1,11)}
print(myset)

mydictionary={"soap":100,"perfume":300,"deo":400,"hairoil":250,"babysoap":100}

myset1={x for x in mydictionary.values()}
print(myset1)

myset2={x for x in mydictionary.keys() if len(x)>3}
print(myset2)
"""
"""products = ["Soap","Perfume","Deo","Hair Oil"]
prices=[100,300,400,250]
mydict = {key:value for (key,value) in zip(products,prices)}
print(mydict)"""

"""
var =500
def myfunc():
    var=100
    print(var)
myfunc()
var = 300
print(var)
"""
"""
def show(var1,var2):
    print(var1,"\t",var2)
    myfun()


def myfun():
    print("inside myfun")

show(10,20)

"""
"""
def main(fun):
    fun()
    print("inside caller function")

def disp():
    print("inside disp function")

main(disp)
"""
""""
def disp1():
    print("inside disp1")
    return disp2

def disp2():
    print("inside disp2")

var1=disp1()
var1()  # here "disp2()" will be called
"""
"""def disp1():
    print("inside disp1")
    return disp2

def disp2():
    print("inside disp2")

disp1()()    # no need to collect the returned function in any variable
"""
#print(dir(__builtins__))
""""
num=10
name="abc"
print("globals are\t",globals())

def outer():
    b=30
    print("locals for outer\t",locals())
    def inner():
        a=15
        print("locals for inner\t", locals())
    inner()

outer()
"""
"""
num=100
var = num
print(num)
del num
print(num)
print(var) #var wont print as well 
"""
"""def hehe():
    print("this is a function from first ")
print("Will print regardless ")
"""
""""
def add(a,b):
    return a+b

if __name__== '__main__' : print(add(10, 20))
print(__name__)
"""
"""add=lambda x,y:x+y
print("add is the reference to the object of type\t",type(add))
print("address of the object where add refers to is\t", id(add))
print(add(5,6))
"""
"""add = lambda x,y:x+y
print(add(10,20))
"""
""""
from multipledispatch import dispatch

@dispatch(int, int)
def add(a, b):
    return a + b

@dispatch()
def add():
    return 10 + 20

print(add())        # This will call the version with no arguments → 30
print(add(5, 7))    # This will call the version with two ints → 12
"""


"""class student :
    def __init__(self,name,age,rollNo):
        self.name = name
        self.age = age
        self.rollNo = rollNo
    def display(self):
        print(self.name,self.age,self.rollNo)
    def __del__(self):
        print("hello")
s1 = student("John",22,1)
s2 = student ("krish",21,23)
s1 = s2
s1.display()
s2.display()
print(type(s1))
print(type(s2))
print (type(student))
"""
"""class First:
    def mainfunction(self):
        print("address of self is\t",id(self))
        print("type of self is\t",type(self))
        print("inside main function")
f1=First()
print("address of f1 is\t",id(f1))
f1.mainfunction()

f2=First()
print("address of f2 is\t",id(f2))
print("let's invoke mainfunction with f2")
f2.mainfunction()
"""

""""
class Base:
    def __init__(self,num):
       self.num=num
    def disp(self):
        print(self.num)
s1=Base(10)
print(s1)
print(type(s1.__init__))
print(type(s1.disp))

class Base:
    def __init__(self,num):
       self.num=num
    def disp(self):
        print(self.num)
s1=Base(10)
print(s1)
print(hasattr(s1,'disp'))
print(hasattr(s1,'__init__'))

"""
""""
from multipledispatch import dispatch


class First:
    @dispatch(int)
    def disp(self, val):
        print(val)

    @dispatch(str)
    def disp(self, val):
        print(val)


f1 = First()
f1.disp("hello")
f1.disp(100)
"""
""""
from multipledispatch import dispatch


class Sample:
    @dispatch(int)
    def __init__(self, num):
        self.num = num

    @dispatch(str)
    def __init__(self, name):
        self.name = name


a1 = Sample(10)
a2 = Sample("Kunal")
print(a1.num)
print(a2.name)
"""
"""
class Account:
    rate=9                  # class variable
    def __init__(self,accid,name,balance):
        self.accid=accid                    # instance variable
        self.name=name                      # instance variable
        self.balance=balance                # instance variable

c1=Account(1,"Abc",40000)
c2=Account(2,"Xyz",70000)
print(c1.accid,"\t",c1.name,"\t",c1.balance)
print(c2.accid,"\t",c2.name,"\t",c2.balance)
c1.balance=43000
c2.balance=78000
print(c1.accid,"\t",c1.name,"\t",c1.balance)
print(c2.accid,"\t",c2.name,"\t",c2.balance)
print(Account.rate,"\t",c1.rate,"\t",c2.rate)
Account.rate=12
print(Account.rate,"\t",c1.rate,"\t",c2.rate)
print(id(c1.name),"\t",id(c2.name))
print(id(Account.rate),"\t",id(c1.rate),"\t",id(c2.rate)) 
"""

"""mylist = [5,6,7,2]
list2 = [2.3,3,3]
for (a,b) in zip(mylist,list2):
    print(a,b)
print(mylist[0:3:2])
list=[i for i in range(1,21) if i%2==0]
print(list)
mylist.sort()
print(mylist)


class Parent:
    def __init__(self):
        print("Hello from parent")

class Child(Parent):
    def __init__(self):
        super().__init__()  # Optional: only if you want to call Parent's constructor too
        print("Hello from the child")

# Create an object of Child
c = Child()
"""
"""class Base:
    def __init__(self,num1):
        self.num1=num1
        print("Base class constructor ",self.num1)
    def disp1(self):       # overridden method
        print("Base class disp1 method")


class Sub(Base):
    def __init__(self):
        super().__init__(100)    # invoking Base class parameterized constructor explicitly
        print("Sub class constructor")

    def disp1(self):      #  overriding method
        print("Sub class disp1 method")

s1 = Sub()
print(id(s1))

s1.disp1()
"""
# multiple inheritance , multiple parents have same method name

"""class Base1:
    def __init__(self,num1):
        self.num1=num1
        print("Base1 class constructor  ",self.num1)
    def disp2(self):
        print("Base1 disp2")

class Base2:
    def __init__(self,num2):
        self.num2=num2
        print("Base2 class constructor   ",self.num2)
    def disp2(self):
        print("Base2 disp2")

class Sub(Base1,Base2):
    def __init__(self):
       Base1.__init__(self,100)
       Base2.__init__(self,300)
       print("Sub class constructor")
    def disp3(self):
        print("Sub disp3")


s1 = Sub()
s1.disp2()  
s1.disp3()
"""
"""def main(fun):
    fun()
    print("inside caller function")
def disp():
    print("inside called function")
main(disp)
"""

"""from abc import ABC, abstractmethod

class Person(ABC):
    def walk(self):
        print("I can walk")
    def talk(self):
        print("I can talk")
    def eat(self):
        print("I can eat")
    def sleep(self):
        print("I can sleep")
    @abstractmethod
    def performduties(self):
        pass

class Teacher(Person):
    def performduties(self):
        print("Perform teacher's duties")

class HouseWife(Person):
    def performduties(self):
        print("Perform HouseWife's duties")

class Soldier(Person):
    def performduties(self):
        print("Perform Soldier's duties")


def perform(ref):
    ref.walk()
    ref.talk()
    ref.eat()
    ref.sleep()
    ref.performduties()


perform(Teacher())
perform(Soldier())
perform(HouseWife())

#ob = Person()   #  TypeError: Can't instantiate abstract class Person with abstract method performduties
"""
#Duck type
""""
class India:
    def capital(self):
        print("New Delhi is the capital of India")
    def language(self):
        print("Hindi is the most widely spoken language of India")
    def type(self):
        print("India is developing country")

class USA:
    def capital(self):
        print("Washington, D.C. is the capital of USA")
    def language(self):
        print("English is the primary language of USA")
    def type(self):
        print("USA is a developed country")


def perform(obj):
    obj.capital()
    obj.language()
    obj.type()

perform(India())
print("Let's pass USA")
perform(USA())
"""
""""
var=5
try:
    print(var/0)
except ZeroDivisionError:
    print("You can't devide any number by 0")
print("done")
mydict = {1:'Krish',2:'ramesh'}
print(mydict[1])
mydict[4] = 'krish2'
print(mydict)
tuple = (1,2,3)
tuple2 = (4,5,6)
print(tuple+tuple2)
"""
""""
def double(var):
	if var<=0:
		raise Exception("IllegalValue Exception")
	return var*var

def fun():
	try:
		print(double(4))
	except Exception as e:
		print("error is\t",e.__str__())
	print("Done")
fun()

"""

# Exception class has following "__init__()" method:

""" 
def __init__(self,message=None)
	self.message=message
"""

""""
class IllegalValue(Exception):
	pass

def double(var):
	if var<=0:
		raise IllegalValue("Number cannot be negative or zero")
		# raise IllegalValue()
	return var*var

def fun():
	try:
		print(double(-4))
	except Exception as e:
		print("error is\t",e.__str__())
	print("Done")
fun()
"""


import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="my_python_db"
)

cursor = conn.cursor()
cursor.execute("SELECT * FROM students")

for row in cursor.fetchall():
    print(row)

conn.close()
"""
#Data Base Handling
import mysql.connector as m
mydatabase=m.connect(host="localhost",user="root",password="krish1209",database="pythondb1")
cursor=mydatabase.cursor()
cursor.execute("use my_python_db")
query="select * from dept"
cursor.execute(query)
result=cursor.fetchall()     # here we get tuples equivalent to the number of records
for record in result:
    print(record)#   commit() is compulsory
    mydatabase.commit()