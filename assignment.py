
list = [1,2,3,4,"habib"]

length = len(list)

for i in range(1,length+1):
    print(list[-i])

list2 = ["abir", "jeshadbro"]

list.extend(list2)
print(list)

list.append("ai")

for i in range(length):
    for j in range(i+1):
        print(j, end="")
    print("")




dic = {
    "name": "Abir",
    "age": 21,
    "gender": "male"
}


print(dic["name"])
print(dic["age"])

work ={
    "Abir" : "daffodil software",
    "hour" : "8 hours"
}

print("Abir works in", work[dic["name"]])


def add(a,b):
    print(f"Adding {a} + {b}")
    return a + b

def subtract(a, b):
    print(f"Subtracting {a} - {b}")
    return a - b

def multiply(a, b):
    print(f"Multiplying {a} * {b}")
    return a * b

def divide(a, b):
    print(f"Dividing {a} / {b}")
    return a / b

print(f"Let's do some math with just functions!")

age = add(20, 2)
height = subtract(78, 4)
weight = multiply(120, 2)
iq = divide(146, 2)

print(age, height, weight, iq)

def add(a, b):
    return a + b
def division(a, b):
    return a / b

result = add(10, 5)
result1 = division(49, 8)
print(result, result1)

def child(child1, child2, child3):
    print("last son is ", child3)

last= child(child1="sansa", child2="arya", child3="bran")



class age:
    def __init__(self, name, age):
        self.name=name
        self.age=age

    def intro(self):
        return self.name


result = age("abir", 21)
result.intro()


class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)


list = [2, 2, 1, 4, 5, 6, 8]
for i in list:
    for j in range(i):
        print(j, end="" )
    print(i)


class identity:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
    def add(self):
        print("you " + self.name, "and gender is " + self.gender)

    men1 = identity("abir", "male")

    men1.add()

list = [1,4,76,9,5,90]

sum=0
try:
    for j in list:
        sum += i
    print(sum)
except Exception as e:
    print(e)


sum = 0
i = 0
while i < 12:
    i += 1
    sum += i
print(sum)
avg = (sum/i)
print(avg)

class Identity:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce_self(self):
        print("i am " + self.name)
        print("and " + self.age)

    def compare(self, per2):
        if per1.age == per2.age:
            print("They are same")
        else:
            print("They are different")
        if per1.name == per2.name:
            print("They are same")
        else:
            print("They are not same")

per1 = Identity("abir", "23")
per2 = Identity("mumu", "23")
per1.introduce_self()
per2.introduce_self()
per1.compare(per2)


class Calculation:

    value = 10
    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        return (self.m1 + self.m2 + self.m3)/3

    def get_m1(self):
        return self.m1

    def set_m1(self, value):
        self.m1 = value

    @classmethod
    def class_value(cls):
        return cls.value

    @staticmethod
    def info():
        print("anything")

average = Calculation(45, 58, 23)
average.set_m1(59)
print(average.avg())
Calculation.class_value()
Calculation.info()


class A:
    def __init__(self):
        print("Class A is working")
    def feature1(self):
        print("Feature 1 is working")

    def feature2(self):
        print("Feature 2 is working")

class B:
    def __init__(self):
        super().__init__()
        print("Class B is working")

    def feature3(self):
        print("Feature 3 is working")

    def feature4(self):
        print("Feature 4 is working")

class C(A, B):
    def __init__(self):
        super().__init__()
        print("Class C is working")

    def feature5(self):
        print("Feature 5 is working")

    def feature6(self):
        print("Feature 6 is working")
     def feat(self):
         super().feature1()
obj = C()
obj.feature1()



class Identity:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll
        self.lap = self.Laptop()
    def show(self):
        print(self.name, self.roll)
        self.lap.show()

    class Laptop:
        def __init__(self):
            self.brand = "HP"
            self.processor = "i5"
            self.ram = "8"
        def show(self):
            print(self.brand, self.processor, self.ram)

studlap = Identity.Laptop()
stu1 = Identity("abir", "21")
stu1.show()

class Inheritance:
    def feature1(self):
        print("Hi")
    def feature2(self):
        print("there")

class Inherit(Inheritance):
    def feature3(self):
        print("paisi")
    def feature4(self):
        print("bro")


class1 = Inherit()

class1.feature1()


class PyCharm:
    def execute(self):
        print("compiling")
        print("running")

class Laptop:
    def code(self, ide):
        ide.execute()

ide = PyCharm()
lap1 = Laptop()
lap1.code(ide)


class Mycharm:
    def execute1(self, ide):
        print("Sentiment analysis")
        print("emotion detect")

class Pycharm:
    def execute(self, ide):
        print("compiling")
        print("running")
        print("Sentiment analysis")
        print("emotion detect")

class Laptop:
    def code(self):
        ide.execute()

ide = Mycharm()
pc1 = Mycharm()
pc1.execute1(ide)



class Robot:
    def intro(self):
        print("This is " + self.name)
        print("This is " + self.age)

r1 = Robot()
r2 = Robot()
r1.name = "abir"
r1.age = "21"
r2.name = "kabir"
r2.age = "22"
r1.intro()
r2.intro()

class Robot:
    def intro(self):
        print("This is " + self.name)
        print("This is " + self.age)
    def add(self):
        print("address is "+ self.loc)

r1 =Robot()
r1.loc = "kazipara"
r1.add()

r1 = Robot()
r1.name = "abir"
r1.age = "21"
r1.intro()


class Person:
    def __init__(self, name: str, birth_year: int, ht: int):
        self.name = name
        self.birth_date = birth_year
        self.height = ht

    def get_name(self):
        return self.name

    def get_birthdate(self):
        return self.birth_date

    def set_name(self, value):
        if self.__has_any_number(value):
            print("Your name contains Numbers")
            return
        self.name = value

    def __has_any_number(self, string):
        return "0" in string


    def get_summery(self):
        return f"Name: {self.name}, Birth Date: {self.birth_date}, Height: {self.height}"

a_person = Person("abir", 1997, 6)
print(a_person.get_summery())
a_person.set_name("0Abir Mahamud")
print(a_person.get_summery())
a_person.name = ("0Abir Mahamud")
print(a_person.name)

person_list = [Person("Kabir", 1998, 7),
               Person("jabir", 1880, 5),
               Person("Nabir", 1999, 6)]

for person in person_list:
    if person.get_birthdate() >= 1990:
        print(person.get_summery())

class Student(Person):
    def __init__(self, name: str, birth_year: int, ht: int):


class Men:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def identity(self):
        print(self.name, self.address)

human = Men("abir", "mirpur")
human.identity()

sum = 0
for i in range(11):
    sum=sum+i
print(sum)

sum = 0
i = 0
while i <= 10:
    sum = sum + i
    i = i + 1
print(sum)


from time import sleep
from threading import *
class Hello(Thread):
    def run(self):
        for i in range(5):
            print("Hello")
            sleep(1)

class Hi(Thread):
    def run(self):
        for i in range(5):
            print("Hi")
            sleep(1)
c1 = Hello()
c2 = Hi()

c1.start()
sleep(0.2)
c2.start()

c1.join()
c2.join()
print("Done :)")


class Calculation:
    def __init__(self, numbers):
        self.numbers=numbers
    def square(self, numbers):
        for i in numbers:
            print("squre: ", i*i)

    def cube(self, numbers):
        for i in numbers:
            print("cube: ", i*i*i)

arr=[2,3,4,5]

calc = Calculation(arr)
calc.square(arr)
calc.cube(arr)



def square(numbers):
    for i in numbers:
        print("squre: ", i * i)

def cube(numbers):
    for i in numbers:
        print("cube: ", i * i * i)


arr = [2, 3, 4, 5]


square(arr)
cube(arr)

class forSelf():
    a = 5
    b = 6

    def setter(self,a,b):
        print(self.a,self.b)
        self.a = a
        self.b = b


    def get(self):
        return self.a,self.b

obj = forSelf()

obj.setter(7,8)
returnvalue = obj.get()
print(obj.a)
print(returnvalue)



dictionary = {}
for i in range(2):
    name = input("Name...")
    id = input("id...")
    add = input("address...")
    dictionary[name] = [id]
    dictionary[id] = [add]
print(dictionary)

arr = []
for i in range(4):
    arr.append(input("Give me value..."))
print(arr)
for i in arr:
    print(i)

"""Importing the required packages"""
import random
import collections
import math
import os
import zipfile
import time
import re
import numpy as np
import tensorflow as tf
from matplotlib import pylab
%matplotlib inline
from six.moves import range
from six.moves.urllib.request import urlretrieve
"""Make sure the dataset link is copied correctly"""
dataset_link = 'http://mattmahoney.net/dc/'
zip_file = 'text8.zip'
def data_download(zip_file):
    if not os.path.exists(zip_file):
        zip_file, _ = urlretrieve(dataset_link + zip_file, zip_file)
        print('File downloaded successfully!')
        return None
data_download(zip_file)