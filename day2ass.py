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
