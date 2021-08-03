print('Hello World')
print("Printing with double quotation marks")
print('Checking if they the same, this has one quotation mark.')

print(2 * (3+4))
print(10/2)
print((4+8)/2)
print(1+2+3+4.0+5)
print(2**5)
print(9**0.5)
print(8**(1/3))

# Floor division

print('Floor division for 20 and 6 = ', 20//6)
print('20 mod 6 = ', 20 % 6)
print(7 % (5//2))
print(0.01*(2**30))

#  String

print("Python is fun!")
print('Always look on the bright side of life')
print('Today is Logan\'s day')
print('Printing\nNew Line at this point\n How do you feel?')
print("""This
is a
multiline
text""")

#  Concatenation

print("spam"+"eggs")
print("spam"+'eggs')
print('spam'*3)
print(4 * '2')

#  Variables
x = 3
print('sx = ', x)
print('x + 3 = ', x + 3)
name = input('What is your name: ')
print('Did you say your name is', name + '?')
print('Alright, nice to meet you',name)
age = int(input('How old are you? '))
print(name, "we need to confirm the fact that you are ", age, ' years old')
#print(num:=int(input()))

f1 = int(input('First integer: '))
f2 = int(input('Second integer: '))
print(f1 + f2)

my_boolean = True
print(my_boolean)

print(2 == 3)
print('hello' == 'hello')
print('hello' == 'Hello')
if 10 > 2:
    print('The boolean value of the statement is', 10 > 2)
if(1==1) and(2+2<3):
    print('true')
elif (1+1>0):
    print('Just jonzing')
else:
    print('Tada')

num = [5, 7, 4, 0, 2]
print(num[0])
List = [2, "name", [4.32, 3.56], "text"]
print(List[2][1])
print(List[3])

strr = "Hello world!"
print(strr[0])

words = ["hello"]
words.append("world")
index = 0
words.insert(index, "Hey there\n")
print(words[1])
print(len(words))
print(words)

x = 1
while x < 10:
    if x % 2 == 0:
        print(x, "is even")
    else:
        print(str(x) + " is odd")
    x += 1

i = 1
while i <= 5:
  print(i)
  i += 1
  if i == 3:
    print("continuing now")
    continue
names = ["Logan", "Edgar", "Tristan"]
for name in names:
    print(name + "!!!")

str = "Coding early in the morning"
count = 0
for x in str:
    if x == "y":
        count += 1
print(count)

numbers = list(range(10))
print (numbers)

numbers = list(range(3, 8))
print(numbers)

print(range(20) == range(1, 20))

numbers = list(range(5, 20, 2))
print(numbers)

list = [1,1,2,3,5,8,13]
print(list[list[4]])


def my_func():
    print('spam' * 3)

my_func()


def word_with_excla(word):
    print(word + '!')


word_with_excla('Logan')
word_with_excla('damn')


def min(x,y):
    if x <= y:
        return x
    else:
        return y


print(min(5, 7))
"""
Doc Strings here. Syntax's or codes here do not run
"""
import random
from math import sqrt as square_roots
for i in range(5):
    value = random.randint(1, 6)
    print(value)

print(square_roots(50))


def print_nums(x):
    for i in range(x):
        print(i)
        return

print_nums(30)

def func(x):
    res = 0
    for i in range(x):
        res += i
    return res

print(func(10))

celsius = int(input())
def conv(celsius):
    c = ((9/5)*(celsius)) + 32
    return c
fahrenheit = conv(celsius)
print(fahrenheit)

try:
    num1 = 7
    num2 = 0
    print(num1/num2)
    print("Calculation complete")
except ZeroDivisionError:
    print("An error occurred")
    print('Cannot divide by zero')

print(1)
#raise TypeError
print('x')

name = '123'
#raise NameError("Invalid type")
print(1)
assert 2 + 2 == 4
print(2)
assert 1+ 1 == 2
print(3)

file = open("text.txt", "r+")
#cont = file.read()
#print(file.read(16))
#print(file.read(10))
#print(file.read())

#print(file.readlines())
for line in file:
    print(line)
file.close()

file = open("text.txt", "w")
file.write("Adding these strings to file")
file.close()

file = open("text.txt")
print(file.read())
file.close()

with open("text.txt") as f:
    print(f.read())

file = open("text.txt", "r")
# str = file.read()
# print(len(str))
for line in file:
    #print(file.read(1))
    print(len(file.readlines()))
file.close()

ages = {
    "Dave": 24,
    "Mary": 30,
    "John": 58,
}
print(ages["Dave"], ages["Mary"], ages["John"])

primary = {
    "red": [255, 0, 0],
    "green": [0, 255, 0],
    "blue": [0, 0, 255],
}
print(primary["red"])

primes = {1: 2, 2: 3, 4: 7, 7:17}
print(primes[primes[4]])

fib = {1: 1, 2: 1, 3: 2, 4: 3}
print(fib.get(4, 0)  + fib.get(7, 5))

#           Tuples
words = ("spam", "eggs", "sausages",)
print(words[0])

#  List slices
square = [0, 1, 4, 9, 12, 14, 25, 64, 81]
print(square[2:6])
print(square[:5])
print(square[3:])

list = ["a", "b", "c", "d"]
a = list[0:2]
print(a)

sqs = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(sqs[1::4])

squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[1:-1])
print(squares[::-1])

# list comprehension
cubes = [i**3 for i in range(10)]
print(cubes)

evens=[i**2 for i in range(10) if i**2 % 2 == 0]
print(evens)

a = [i for i in range(20) if i % 3 == 0]
print(a)

print("{0}{1}{0}".format("abra", "cad"))


filename = input("Enter a filename: ")

with open(filename) as f:
   text = f.read()

print(text)

nums = (55, 44, 33, 22)
print(max(min(nums[:2]), abs(-42)))

text = input().split()
length = [len(x) for x in text]
maximum = max(length)
text_index = length.index(maximum)
print(text[text_index])

def test(func, arg):
    return func(func(arg))
def mult(x):
    return x * x
print(test(mult, 2))
def polynomial(x):
    return x**2 + 5*x + 4
print(polynomial(-4))
print((lambda x: x**2 + 5*x + 4)(-4))

double = lambda x: x**2
print(double(7))

def add_five(x):
    return x + 5


nums = [11, 22, 33, 44, 55]
result = list(map(add_five, nums))
print(result)

nums = [11, 22, 33, 44, 55]
result = list(map(lambda x: x+5, nums))
print(result)

nums = [11, 22, 33, 44, 55]
res = list(filter(lambda x: x%2 ==0, nums))
print(res)

def countdown():
    i=5
    while i > 0:
        yield i
        i -= 1

for i in countdown():
    print(i)

def make_word():
  word = ""
  for ch in "spam":
    word +=ch
    yield word

print(list(make_word()))

def decor(func):
    def wrap():
        print("============")
        func()
        print("============")
    return wrap

def print_text():
    print("Hello world!")

decorated = decor(print_text)
decorated()


def decor(func):
    def wrap():
        print("============")
        func()
        print("============")
    return wrap


@decor
def print_text():
    print("Hello world!")

print_text();

def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x-1)
print(factorial(5))

def is_even(x):
    if x == 0:
        return True
    else:
        return is_odd(x-1)

def is_odd(x):
    return not is_even(x)


print(is_odd(17))
print(is_even(23))


def fib(x):
  if x == 0 or x == 1:
    return 1
  else:
    return fib(x-1) + fib(x-2)
print(fib(4))

num_set = {1, 2, 3, 4, 5}
word_set = set(["spam", "eggs", "sausage"])

print(3 in num_set)
print("spam" not in word_set)

first = {1, 2, 3, 4, 5, 6}
second = {4, 5, 6, 7, 8, 9}

print(first | second)
print(first & second)
print(first - second)
print(second - first)
print(first ^ second)

from itertools import accumulate, takewhile

nums = list(accumulate(range(8)))
print(nums)
print(list(takewhile(lambda x: x<= 6, nums)))


from itertools import product
a={1, 2}
print(len(list(product(range(3), a))))
nums = {1, 2, 3, 4, 5, 6}
nums = {0, 1, 2, 3} & nums
nums = filter(lambda x: x > 1, nums)
print(len(list(nums)))


def power(x, y):
    if y == 0:
        return 1
    else:
        return x * power(x, y - 1)


print(power(2, 3))

x, y, n = 0, 1, int(input(""))
for i in range(n):
    print(x)
    x, y = y, x+y

class Juice:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
    def __str__(self):
        return (self.name + " (" + str(self.capacity) + "L)")
    def __add__(self, other):
        self.capacity = self.capacity + other.capacity
        self.name = self.name + "&" + other.name
        return (self.name + " (" + str(self.capacity) + "L)")
x = Juice("Orange", 1.5)
y = Juice("Apple", 2.0)
result = x + y
print(result)

import re

str = "My name is David. Hi David."
pattern = r"David"
newstr = re.sub(pattern, "Amy", str)
print(newstr)

import re

pattern = r"gr.y"

if re.match(pattern, "grey"):
    print("Match 1")

if re.match(pattern, "gray"):
    print("Match 2")

if re.match(pattern, "blue"):
    print("Match 3")

import re

pattern = r"[aeiou]"

if re.search(pattern, "grey"):
    print("Match 1")

if re.search(pattern, "qwertyuiop"):
    print("Match 2")

if re.search(pattern, "rhythm myths"):
    print("Match 3")

import re
n = input()
if re.match(r"^[189]",n) and len(n) == 8:
    print("Valid")
else:
    print("Invalid")


import this
a, b, c, d, *e, f, g = range(20)
print(len(e))

for i in range(10):
   if i > 5:
      print(i)
      break
else:
   print("7")

for i in range(10):
  try:
    if 10 / i == 2.0:
      break
  except ZeroDivisionError:
    print(1)
  else:
    print(2)

def concatenate(*args):
    v = []
    for i in args:
        x = v.append(i)
    y = "-".join(v)
    return y
print(concatenate("I", "love", "Python", "!"))