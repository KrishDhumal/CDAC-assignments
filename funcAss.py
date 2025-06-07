#Question 1
"""
def add():
    print("can Add")
def modify():
    print ("can modify")
def delete():
    print("can delete")
a = int(input("Enter a number"))
if(a==1):
    add()
elif(a==2):
    modify()
else:
    delete()
    """
#Question 2
""""
def square (x):
    return x*x
x = int(input("Enter a number"))
print(square(x))
"""
""""
#Question 3
def acceptor(any):
    print(any)
any = (input("Enter anything"))
acceptor(any)
"""
#Question 4
"""
def myFun():
    print("krish dhumal says hi ")
def myFun2():
    print("time to call func 1")
    myFun()
myFun2()
"""
#Question 5
""""
def numbCheck(x):
    if(x>=1):
        return 1
    elif(x<0):
        return -1
    else:
        return 0
x = int(input("Enter a number"))
print(numbCheck(x))
"""
#Question 6
""""
def toggleChar(ch):
    if ch.islower():
        return ch.upper()
    else:
        return ch.lower()
ch = input("Enter a character: ")
print(toggleChar(ch))
"""
#Question 7
"""
def toggleString(s):
    return s.swapcase()
s = input("Enter a string: ")
print(toggleString(s))
"""

#Question 8
"""

def acceptChars(a, b, c, d="", e=""):
    print("Characters entered:", a, b, c, d, e)
acceptChars('A', 'B', 'C')
acceptChars('X', 'Y', 'Z', 'P')
acceptChars('1', '2', '3', '4', '5')
"""
""""
#Question 9

def sumAll(*args):
    total = sum(args)
    print("Sum is:", total)
sumAll(1, 2, 3)
sumAll(10, 20, 30, 40, 50)


"""
