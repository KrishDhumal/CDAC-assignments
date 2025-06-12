# Question 1
"""
lst = []
num = int(input("Enter a number: "))
name = input("Enter a name: ")
flt = float(input("Enter a float value: "))
lst.extend([num, name, flt])

new_name = input("Enter another name to insert at 2nd position: ")
lst.insert(1, new_name)

num_to_append = int(input("Enter a number to append at the end: "))
lst.append(num_to_append)

print("Final list:", lst)
"""

# Question 2
"""
lst = []
while True:
    num = int(input("Enter a number (0 to stop): "))
    if num == 0:
        break
    lst.append(num)

print("List:", lst)
print("Length of list:", len(lst))
"""

# Question 3
"""
lst = []
print("Enter 5 numbers:")
for _ in range(5):
    lst.append(int(input()))

print("List before extend:", lst)

lst.extend([10, 20, 30])  # Hardcoded additional numbers

print("List after extend:", lst)
"""

# Question 4
"""
lst = []
num = int(input("Enter a number: "))
string = input("Enter a string: ")
flt = float(input("Enter a decimal value: "))
bool_val = input("Enter boolean value (True/False): ") == 'True'
char = input("Enter a single character: ")

lst.extend([num, string, flt, bool_val, char])

print("List from beginning:", lst)
print("List from end:", lst[::-1])
"""

# Question 5
"""
lst = []
print("Enter 5 numbers:")
for _ in range(5):
    lst.append(int(input()))

num_to_remove = int(input("Enter number to remove: "))
if num_to_remove in lst:
    lst.remove(num_to_remove)
else:
    print("Number not found in list")

print("Updated list:", lst)
"""

# Question 6
"""
lst = []
print("Enter 5 numbers:")
for _ in range(5):
    lst.append(int(input()))

pos = int(input("Enter position to remove (1-based index): "))
if 1 <= pos <= len(lst):
    lst.pop(pos-1)
else:
    print("Invalid position")

print("Updated list:", lst)
"""

# Question 7
"""
lst = ["hello", 123, 'A', True, 45.67]

print("a) Reverse order:", lst[::-1])
print("b) Elements from 2nd position:", lst[1:])
print("c) Elements from 1st to 3rd position:", lst[0:3])
print("d) Slice 1st to 3rd elements from the end:", lst[-3:-0] if len(lst) >=3 else lst)
"""

# Question 8
"""
# Using list comprehension
lst = [i for i in range(1, 21)]
odd_lst = [x for x in lst if x % 2 != 0]

print("List 1 to 20:", lst)
print("Odd numbers from list:", odd_lst)
"""

# Question 9
"""
names = []
print("Enter 5 names:")
for _ in range(5):
    names.append(input())

names.sort()
print("Sorted ascending:", names)

names.sort(reverse=True)
print("Sorted descending:", names)
"""

# Question 10
"""
class Car:
    def __init__(self, model, isautomatic):
        self.model = model
        self.isautomatic = isautomatic

    def get_model(self):
        return self.model

    def get_isautomatic(self):
        return self.isautomatic

# Create car objects
cars = [
    Car("Toyota", True),
    Car("Honda", False),
    Car("BMW", True),
    Car("Ford", False),
    Car("Audi", True),
    Car("Kia", False)
]

print("All cars:")
for car in cars:
    print(f"Model: {car.get_model()}, Automatic: {car.get_isautomatic()}")

# Filter cars where isautomatic is True
automatic_cars = [car for car in cars if car.get_isautomatic()]

print("\nAutomatic cars:")
for car in automatic_cars:
    print(f"Model: {car.get_model()}, Automatic: {car.get_isautomatic()}")
"""


#TUPLE Questions

# Question 1
"""
lst = [10, 20, 30, (40, 50), 60]
count = 0
for item in lst:
    if isinstance(item, tuple):
        break
    count += 1
print("Count before tuple:", count)
"""

# Question 2
"""
tup = (23, 5, 89, 12, 47)
asc = tuple(sorted(tup))
desc = tuple(sorted(tup, reverse=True))
print("Original tuple:", tup)
print("Sorted ascending:", asc)
print("Sorted descending:", desc)
"""

# Question 3
"""
tup = (1, 2, 3, 2, 4, 5, 1, 6, 2)
repeated = set([x for x in tup if tup.count(x) > 1])
print("Repeated items:", repeated)
"""


#SET questions
# Question 1
"""
s = set()
print("Enter 10 values:")
for _ in range(10):
    val = input()
    s.add(val)

remove_val = input("Enter a value to remove: ")
s.discard(remove_val)

print("Updated set:", s)
"""

#String Questions

# Question 1
"""
s = input("Enter a string: ")
if s == s[::-1]:
    print("It is a palindrome")
else:
    print("It is not a palindrome")
"""

# Question 2
"""
s = input("Enter a string: ")
start = int(input("Enter start index: "))
end = int(input("Enter end index: "))
print("Sliced string:", s[start:end])
"""

# Question 3
"""
s = input("Enter a string: ")
vowels = 'aeiouAEIOU'
count = sum(1 for ch in s if ch in vowels)
print("Number of vowels:", count)
"""

# Question 4
"""
s = input("Enter a string: ")
repeated = set()
for ch in s:
    if s.count(ch) > 1:
        repeated.add(ch)
print("Repeated characters:", repeated)
"""

# Question 5
"""
s = input("Enter a string: ")
words = s.split()
print("Number of words:", len(words))
"""

# Question 6
"""
s = input("Enter a sentence: ")
words = s.split()
reversed_sentence = ' '.join(reversed(words))
print("Reversed sentence:", reversed_sentence)
"""

# Question 7
"""
def is_pangram(sentence):
    sentence = sentence.lower()
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    return alphabet.issubset(set(sentence))

s = input("Enter a sentence: ")
if is_pangram(s):
    print("It is a pangram")
else:
    print("It is not a pangram")
"""

#Dictonary Question
# Question 1
"""
students = {}
for i in range(1, 6):
    name = input(f"Enter name of student {i}: ")
    students[i] = name
print("Student dictionary:", students)
"""

# Question 2
"""
products = {'soap': 100, 'deo': 300, 'perfume': 400}
product_name = input("Enter product name: ").lower()
price = products.get(product_name)
if price is not None:
    print("Price:", price)
else:
    print("product not available")
"""

# Question 3
"""
class Student:
    def __init__(self, name, age, address, qualification):
        self.name = name
        self.age = age
        self.address = address
        self.qualification = qualification

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Address: {self.address}, Qualification: {self.qualification}"

s1 = Student("Amit", 21, "Delhi", "B.Sc")
s2 = Student("Sara", 22, "Mumbai", "B.Tech")
s3 = Student("John", 20, "Chennai", "B.Com")
s4 = Student("Riya", 23, "Kolkata", "M.Sc")

students_dict = {
    1: s1,
    2: s2,
    3: s3,
    4: s4
}

rollno = int(input("Enter roll number: "))
student = students_dict.get(rollno)
if student:
    print(student)
else:
    print("student not found")
"""

# Question 4
"""
people = {'Arham': 'Blue', 'Lisa': 'Yellow', 'Vinod': 'Purple', 'Jenny': 'Pink'}

print("1. Number of students:", len(people))

people['Lisa'] = 'Green'
print("2. Lisa's new favourite colour:", people['Lisa'])

people.pop('Jenny')
print("3. Dictionary after removing Jenny:", people)

print("4. Sorted students and their colours:")
for name in sorted(people):
    print(name, ":", people[name])
"""

#List_Dicotnary
# Question 1
"""
d = {
    'x': list(range(11, 20)),
    'y': list(range(21, 30)),
    'z': list(range(31, 40))
}
print(d['x'][4])
print(d['y'][4])
print(d['z'][4])
"""

# Question 2
"""
d = {0: 10, 1: 20}
d[2] = 30
print(d)
"""

# Question 3
"""
d = {'a': 1, 'b': 2}
key = input()
if key in d:
    print("Key exists.")
else:
    print("Key does not exist.")
"""

# Question 4
"""
data = [
    {'id': 1, 'success': True, 'name': 'Lary'},
    {'id': 2, 'success': False, 'name': 'Rabi'},
    {'id': 3, 'success': True, 'name': 'Alex'}
]
count = 0
for item in data:
    if item.get('success') == True:
        count += 1
print(count)
"""

# Question 5
"""
keys = ['Class-V', 'Class-VI', 'Class-VII', 'Class-VIII']
values = [1, 2, 2, 3]
result = {}
for i in range(len(keys)):
    key = keys[i]
    val = values[i]
    if key not in result:
        result[key] = set()
    result[key].add(val)
print(result)
"""

# Question 6
"""
d = {}
if len(d) == 0:
    print("Dictionary is empty")
else:
    print("Dictionary is not empty")
"""

# Question 7
"""
from collections import Counter
d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}
c1 = Counter(d1)
c2 = Counter(d2)
result = c1 + c2
print(result)
"""

# Question 8
"""
mydictionary1 = {
    'Names': ['Rohit', 'Ganesh', 'SRK', 'Akshay'],
    'age': 40,
    'addresses': ['Mumbai', 'Delhi', 'Kolkara', 'Banglore'],
    'emails': ['actor.gmail.com', 'movie.gmail.com']
}
total = 0
for v in mydictionary1.values():
    if isinstance(v, list):
        total += len(v)
print(total)
"""

# Question 9
"""
s = 'w3resource'
d = {}
for ch in s:
    d[ch] = d.get(ch, 0) + 1
print(d)
"""

# Question 10
"""
mydictionary = {1:'xyz', 3:'abc', 5:'pqr', 2:'xzz'}
for k, v in mydictionary.items():
    print(k, v)
print(len(mydictionary))
"""

# Question 11
"""
d = {'a': 100, 'b': 200, 'c': 50}
print(max(d.values()))
print(min(d.values()))
"""

# Question 12
"""
prnnos = [1, 2, 3, 4, 5, 6]
names = ['abc', 'def', 'pqr', 'lmn', 'xyz', 'uvw']
d = dict(zip(prnnos, names))
print(d)
"""

# Question 13
"""
x = {'key1': 1, 'key2': 3, 'key3': 2}
y = {'key1': 1, 'key2': 2}
for k in x:
    if k in y and x[k] == y[k]:
        print(f"{k}: {x[k]} is present in both x and y")
"""

# Question 14
"""
Players = {
    'Rohit': {'runs': 10000, 'centuries': 15},
    'Virat': {'runs': 12000, 'centuries': 18}
}
for player, stats in Players.items():
    print(player)
    for stat_key, stat_val in stats.items():
        print(stat_key, ":", stat_val)
"""

# Question 15
"""
d = {'a': 1, 'b': 2, 'c': 3}
key = input()
if key in d:
    del d[key]
print(d)
"""

# Question 16
"""
Students = {'d 01': 'Abc', 'd 0 2': 'Xyz', 'd0 3': 'Pqr'}
cleaned = {k.replace(" ", ""): v for k, v in Students.items()}
print(cleaned)
"""

# Question 17
"""
d = {'a': 10, 'b': 20, 'c': 30}
print(sum(d.values()))
"""

# Question 18
"""
mydictionary1 = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36}
mydictionary2 = {7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144}
mydictionary1.update(mydictionary2)
print(mydictionary1)
"""

# Question 19
"""
dic1 = {1:10, 2:20}
dic2 = {3:30, 4:40}
dic3 = {5:50, 6:60}
new_dic = {}
new_dic.update(dic1)
new_dic.update(dic2)
new_dic.update(dic3)
print(new_dic)
"""

# Question 1
"""
create 3 functions "show1()","show2()" and "show3()"
now define a function "caller" in such a way that it can accept any function as an argument and invoke the same.
invoke caller function by passing show1, show2 and show3


def show1():
    print("Inside show1")

def show2():
    print("Inside show2")

def show3():
    print("Inside show3")

def caller(f):
    f()

caller(show1)
caller(show2)
caller(show3)
"""

# Question 2
"""
define nested function and show how will you invoke it.


def outer():
    print("Inside outer function")
    def inner():
        print("Inside inner function")
    inner()

outer()
"""