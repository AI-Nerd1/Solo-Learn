# # print('Hello World')
# # print("Printing with double quotation marks")
# # print('Checking if they the same, this has one quotation mark.')
# #
# # print(2 * (3+4))
# # print(10/2)
# # print((4+8)/2)
# # print(1+2+3+4.0+5)
# # print(2**5)
# # print(9**0.5)
# # print(8**(1/3))
# #
# # # Floor division
# #
# # print('Floor division for 20 and 6 = ', 20//6)
# # print('20 mod 6 = ', 20 % 6)
# # print(7 % (5//2))
# # print(0.01*(2**30))
# #
# # #  String
# #
# # print("Python is fun!")
# # print('Always look on the bright side of life')
# # print('Today is Logan\'s day')
# # print('Printing\nNew Line at this point\n How do you feel?')
# # print("""This
# # is a
# # multiline
# # text""")
# #
# # #  Concatenation
# #
# # print("spam"+"eggs")
# # print("spam"+'eggs')
# # print('spam'*3)
# # print(4 * '2')
# #
# # #  Variables
# # x = 3
# # print('sx = ', x)
# # print('x + 3 = ', x + 3)
# # name = input('What is your name: ')
# # print('Did you say your name is', name + '?')
# # print('Alright, nice to meet you',name)
# # age = int(input('How old are you? '))
# # print(name, "we need to confirm the fact that you are ", age, ' years old')
# # #print(num:=int(input()))
# #
# # f1 = int(input('First integer: '))
# # f2 = int(input('Second integer: '))
# # print(f1 + f2)
#
# # my_boolean = True
# # print(my_boolean)
# #
# # print(2 == 3)
# # print('hello' == 'hello')
# # print('hello' == 'Hello')
# # if 10 > 2:
# #     print('The boolean value of the statement is', 10 > 2)
# # if(1==1) and(2+2<3):
# #     print('true')
# # elif (1+1>0):
# #     print('Just jonzing')
# # else:
# #     print('Tada')
# #
# # num = [5, 7, 4, 0, 2]
# # print(num[0])
# # List = [2, "name", [4.32, 3.56], "text"]
# # print(List[2][1])
# # print(List[3])
# #
# # strr = "Hello world!"
# # print(strr[0])
# #
# # words = ["hello"]
# # words.append("world")
# # index = 0
# # words.insert(index, "Hey there\n")
# # print(words[1])
# # print(len(words))
# # print(words)
# #
# # x = 1
# # while x < 10:
# #     if x % 2 == 0:
# #         print(x, "is even")
# #     else:
# #         print(str(x) + " is odd")
# #     x += 1
# #
# # i = 1
# # while i <= 5:
# #   print(i)
# #   i += 1
# #   if i == 3:
# #     print("continuing now")
# #     continue
# # names = ["Logan", "Edgar", "Tristan"]
# # for name in names:
# #     print(name + "!!!")
# #
# # str = "Coding early in the morning"
# # count = 0
# # for x in str:
# #     if x == "y":
# #         count += 1
# # print(count)
# #
# # numbers = list(range(10))
# # print (numbers)
#
# # numbers = list(range(3, 8))
# # print(numbers)
# #
# # print(range(20) == range(1, 20))
# #
# # numbers = list(range(5, 20, 2))
# # print(numbers)
# #
# # list = [1,1,2,3,5,8,13]
# # print(list[list[4]])
#
#
# def my_func():
#     print('spam' * 3)
#
# my_func()
#
#
# def word_with_excla(word):
#     print(word + '!')
#
#
# word_with_excla('Logan')
# word_with_excla('damn')
#
#
# def min(x,y):
#     if x <= y:
#         return x
#     else:
#         return y
#
#
# print(min(5, 7))
# """
# Doc Strings here. Syntax's or codes here do not run
# """
# import random
# from math import sqrt as square_roots
# for i in range(5):
#     value = random.randint(1, 6)
#     print(value)
#
# print(square_roots(50))
#
#
# def print_nums(x):
#     for i in range(x):
#         print(i)
#         return
#
# print_nums(30)
#
# def func(x):
#     res = 0
#     for i in range(x):
#         res += i
#     return res
#
# print(func(10))

# celsius = int(input())
# def conv(celsius):
#     c = ((9/5)*(celsius)) + 32
#     return c
# fahrenheit = conv(celsius)
# print(fahrenheit)

# try:
#     num1 = 7
#     num2 = 0
#     print(num1/num2)
#     print("Calculation complete")
# except ZeroDivisionError:
#     print("An error occurred")
#     print('Cannot divide by zero')

# print(1)
# raise TypeError
# print('x')

# name = '123'
# raise NameError("Invalid type")
# print(1)
# assert 2 + 2 == 4
# print(2)
# assert 1+ 1 == 2
# print(3)

# file = open("text.txt", "r+")
# #cont = file.read()
# #print(file.read(16))
# #print(file.read(10))
# #print(file.read())
#
# #print(file.readlines())
# for line in file:
#     print(line)
# file.close()

# file = open("text.txt", "w")
# file.write("Adding these strings to file")
# file.close()
#
# file = open("text.txt")
# print(file.read())
# file.close()
#
# with open("text.txt") as f:
#     print(f.read())

# file = open("text.txt", "r")
# # str = file.read()
# # print(len(str))
# for line in file:
#     #print(file.read(1))
#     print(len(file.readlines()))
# file.close()

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