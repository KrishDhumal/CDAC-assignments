#Question 1 
"""a = int(input("Enter a number :"))
for i in range(11):
    res = a*i
    print(res)
"""
#Question 2
"""
ch = input("Enter a character:")
def isVowel(ch):
    match ch:
        case 'a':
            return print("Is a vowel")
        case 'e':
            return print("Is a vowel")
        case 'i':
            return print("Is a vowel")
        case 'o':
            return print("Is a vowel")
        case 'u':
            return print("Is a vowel")
        case _:
            return print("Is a consonent")
isVowel(ch)
"""
#Question 3
"""
count = 1 
while count<11:
    print(count)
    count +=1
    """

#Question 4 
"""
i = 3
while i <= 30:
    if i == 24:
        i += 1
        continue
    print(i)
    i += 1
"""
#Question 5 
"""
marks = int(input("Enter marks (0-100): "))

if marks < 35:
    print("Fail")
elif marks < 50:
    print("Pass")
elif marks < 60:
    print("Second Class")
elif marks < 75:
    print("First Class")
elif marks <= 100:
    print("Distinction")
else:
    print("Invalid marks")
"""
#Question 6 
"""
total = 0
for i in range(1, 11):
    total += i
print("Total of first 10 numbers:", total)
"""

#Question 7
"""
total = 0
while True:
    num = int(input("Enter a number (0 to stop): "))
    if num == 0:
        break
    total += num
print("Total of all numbers entered:", total)
"""

#Question 8 
"""
ch = input("Enter a character: ")
if ch.isupper():
        print("Uppercase alphabet")
elif ch.islower():
        print("Lowercase alphabet")
else:
        print("Not an alphabet")
"""

#Question 9:
"""
print("Question 9: Fibonacci series of 10 numbers")
a, b = 0, 1
count = 0
while count < 10:
    print(a, end=' ')
    a, b = b, a + b
    count += 1
print("\n")
"""

#Question 10: 
"""
print("Question 10: Prime numbers from 3 to 30")
for num in range(3, 31):
    if num > 1:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                break
        else:
            print(num, end=' ')
print("\n")
"""

#Question 11: 
"""
print("Question 11: Check if a number is prime or not")
num = int(input("Enter a number: "))
if num <= 1:
    print(f"{num} is not a prime number")
else:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            print(f"{num} is not a prime number")
            break
    else:
        print(f"{num} is a prime number")
print("\n")
"""

#Question 12: 
"""
print("Question 12: Pattern")
for i in range(1, 6):
    print("* " * i)
print("\n")
"""

#Question 13: 
"""
print("Question 13: Inverted Pattern")
for i in range(5, 0, -1):
    print("* " * i)
print("\n")
"""

#Question 14: 
"""
print("Question 14: Right Aligned Increasing Pattern")
for i in range(1, 6):
    print(" " * (5 - i) + "* " * i)
print("\n")
"""

#Question 15: 
"""
print("Question 15: Right Aligned Pattern with Spaces")
for i in range(1, 6):
    print(" " * (6 - i) + "* " * i)
print("\n")
"""

#Question 16: 
"""
print("Question 16: Inverted Right Aligned Pattern")
for i in range(5, 0, -1):
    print("  " * (5 - i) + "*   " * i)
print("\n")
"""

#Question 17: 
"""
print("Question 17: Diamond Pattern")
n = 6
for i in range(1, n + 1):
    print(" " * (n - i) + "* " * i)
for i in range(n - 1, 0, -1):
    print(" " * (n - i) + "* " * i)
print("\n")
"""
