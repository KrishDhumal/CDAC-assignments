# Question 1
"""
a) normal function

def square(num):
    return num * num
print(square(5))
"""
"""
b) lambda

square_lambda = lambda num: num * num
print(square_lambda(5))

"""
# Question 2
"""
a) normal function

def greet():
    print("Hello World")
greet()
"""
"""
b) lambda

greet_lambda = lambda: print("Hello World")
greet_lambda()

"""
# Question 3
"""
a) normal function

def show(name, age=20):
    print(name, age)
show("Ram")
show("Sita", 25)
"""
"""
b) lambda

show_lambda = lambda name, age=20: print(name, age)
show_lambda("Ram")
show_lambda("Sita", 25)

"""
# Question 4
"""
a) normal function

def display(*args):
    for item in args:
        print(item)
display(1, 2, 3, 4)
"""
"""
b) lambda

display_lambda = lambda *args: [print(item) for item in args]
display_lambda(1, 2, 3, 4)
"""
""""
# how to read from a file


with open("funcAss.py","r") as f:
    data=f.read()
    print(data)

print("Done")
"""
