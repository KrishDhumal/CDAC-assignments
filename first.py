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