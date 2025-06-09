"""sum = 0
for i in range(5):
    sum += i
print(sum)
for i in range(1,10):
    print(i)"""
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
add = lambda x,y:x+y
print(add(10,20))
