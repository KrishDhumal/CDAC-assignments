# Question 1
"""
lst = []
num = int(input("Enter a number: "))
name = input("Enter a name: ")
flt = float(input("Enter a float value: "))
lst.extend([num, name, flt])

new_name = input("Enter another name to insert at 2nd position: ")
lst.insert(1, new_name)  # 2nd position index is 1

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
