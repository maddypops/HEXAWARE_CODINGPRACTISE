x=10
print (x)

a=20
b='hexaware'
print (a,b)


x='technical'
print (x)


c="welcome to hexaware"
def func ():
    c= 'are you an HR'
    print (c)

func()
print (c)


x=90
y=-10
print (type(x),type(y))


r=45.6
print(type(r))


v=2>6
print(type(v))
print(v)


x='maddy'
print(type(x))


x=10+6j
print(type(x))


#if statement
x=12
if x%3==0:
    print('x is divisible by 3')
else:
    print('x is not divisible by 3')


x=int(input('enter the number = '))
if x%2==0:
    print (f"{x} is divisible by 2")
else:
    print (f"{x} is not divisible by 2")



x=int(input('give me a number ='))
if x%2==0:
    print (x,'is even')
elif x==0:
    print(x,'is zero')
else:
    print(x,'is odd')


a= int(input('enter the number = '))
if a>1:
    for i in range(2,a):
        if a%i==0:
            print(a,'is not prime number')
        else:
            print(a,'is prime number')
else:
    print(a,'is less than 1')


list=[1,2,3,4,5]
for i in list:
    print(i)

x="MADHANSAI"
for i in x[0:5]:
    print(i)


i=0
while i>10:
    print(i)
    i+=1


for i in range(1,10):
    for j in range(i):
        print(i,end=' ')
    print()



for i in "MADHANSAI":
    if i=="N":
        break
    print(i)
print("loop has ended")



for i in "MADHANSAI":
    if i=="N":
        continue
    print(i)
print("loop continue")



for i in "MADHANSAI":
    if i=="N":
        pass
        print("pass executed")
    print(i)
print("loop has ended")


name = "MADHANSAIsj"
clean = name.strip().title()
print(clean)

s = "encomotology"
vowels = sum(s.count(v) for v in "aeiou")
print(vowels)

import string
tbl = str.maketrans({d: "*" for d in string.digits})
print("Phone: 123-456".translate(tbl))

words = ["apple", "banana", "cherry"]
print(", ".join(words))

name, age = "Alice", 30
print(f"{name.upper()} is {age} years old.")



##################################################################

list=[1,2,3,4,5]
for i in list:
    if i%2==0:
        print(f"{i} is even")
    else:
        print(f"{i} is odd")


for i in range(1,7):
    if i==6:
        print("found 6 breaking loop")
        break
else:
    print("loop executed without breaking loop")


a=int(input('enter the number = '))
b=int(input('enter the number ='))
if a>10:
    print(f"{a} is greater than 10")
    if b>20:
        print(f"{b} is greater than 20")




ages = [78, 34, 17, 47, 9]
has_license = True

for age in ages:
    if age >= 18 and has_license:
        print(f"Age {age}: Allowed to drive.")
    else:
        print(f"Age {age}: Not allowed to drive.")



def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

num = int(input("Enter a number for recursive factorial: "))
if num < 0:
    print("Factorial not defined for negative numbers.")
else:
    print(f"Factorial of {num} is {factorial(num)}")



n = int(input("Enter how many Fibonacci numbers to print: "))
a, b = 0, 1
if n <= 0:
    print("Enter a positive number.")
elif n == 1:
    print(a)
else:
    print("Fibonacci sequence:")
    for i in range(n):
        print(a, end=' ')
        a, b = b, a + b



sports=['cricket','chess','football','vollyball','basketball']
sports[3]=30.5
print(sports)

sports.append('batmitten')
print(sports)


for i in range (len(sports)):
    if sports[i]==30.5:
        sports[i]='swimming'
print(sports)


sports.remove('batmitten')
print(sports)

x=sports.pop()
print(sports)

x=sports.pop(-1)
print(sports)

tuple=('apple','banana','cherry','mango')

y=tuple[1]
print(y)

hexa=list(tuple)
print(hexa)

a_list=[]
for i in tuple:
    a_list.append(i)
print(a_list)

#............dictionary.........#

student={"name":'madhan', 'age':30, 'department':'CSE'}
print(student['name'])


student['name']='Madhansai'
print(student['name'])


student['college']='vels'
print(student)

b=[]
for student,details in student.items():
    if details=='vels':
        x.append(student)
print(x)



set1={'apple','banana','cherry','mango'}
print(set1)

set1.add('apple')
print(set1)

for i in set1:
    if 'apple' in set1:
        print(i)

#..........DATETIME.............

import time
print('start')
time.sleep(1)
print('end')


from datetime import datetime
timestamp=1234567890
dt=datetime.fromtimestamp(timestamp)
print(dt)


#............FUNCTION..............

def hexa1():
    print('my name is hexa')
hexa1()


def hexa2(name):
    print('my name is ', name)
hexa2(input('enter your name : '))


def add(a,b):
    return a+b
result=add(10,2)
print(result)



def add(a,b):
    return a-b , a*b, a/b
result=add(10,2)
print(result)

def divide(a,b):
    if b!=0:
        return a/b
    else:
        print('division by zero not possibel')
result=divide(10,4)
print(result)


fruits = ["apple", "banana", "cherry", "apple"]
print("Original:", fruits)

fruits.append("date")
print("After append:", fruits)

fruits.remove("banana")
print("After remove:", fruits)

fruits[1] = "blueberry"
print("After modify:", fruits)

print("Iterate:")
for f in fruits:
    print("-", f)



#........vote tracking system.......

visitors=['madhan','ebron','giri','muthu','madhan']
print('visitors', visitors)

voted=set()
for v in visitors:
    if v in voted:
        print(f'{v} is voted')
    else:
        print(f'{v} cast voted')
        voted.add(v)
print('total voted:', len(voted))
print('voters list:', voted)


#..............................................

def find_longest_string(strings):
    longest = ""
    for s1 in strings:
        if len(s1) > len(longest):
            longest = s1
    return longest

def filter_greater_than_five(nums):
    return [n1 for n1 in nums if n1 > 5]

def find_duplicates(values):
    seen, duplicates = set(), []
    for v1 in values:
        if v1 in seen:
            duplicates.append(v1)
        else:
            seen.add(v1)
    return duplicates

words = ["hi", "hello", "world!"]
numbers = [1, 6, 8, 3, 4, 8]
mix = [2, 3, 2, 5, 3]
print("Longest word:", find_longest_string(words))
print("Filtered (>5):", filter_greater_than_five(numbers))
print("Duplicates in mix:", find_duplicates(mix))



class Company:
    name = "XYZ Bank"
    turnover = 5000
    revenue = 1000
    num_employees = 100
    @classmethod
    def productivity(cls):
        return cls.turnover / cls.num_employees
c = Company()
print("Productivity:", Company.productivity())


class car:
    def __init__(self, color, model, engine_type='petrol'):
        self.color = color
        self.model = model
        self.engine_type = engine_type

    def accelerate(self):
        print(f'{self.model} is accelerating')

class electriccar(car):
    def __init__(self, color, model, battery_kwh):
        super().__init__(color, model,engine_type='electric')
        self.battery_kwh = battery_kwh

    def charge(self):
        print(f'{self.model} is charging')

ecar = electriccar('red', 'leaf',40)
ecar.accelerate()
ecar.charge()


class Student:
    def __init__(self, student_id, student_name):
        self.student_id = student_id
        self.student_name = student_name

    def display(self):
        print(f"ID: {self.student_id}, Name: {self.student_name}")

s1 = Student(101, "Madhan")
s1.display()



class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def compute_area(self):
        return self.length * self.width

r1 = Rectangle(10, 5)
print("Area of rectangle:", r1.compute_area())



class Employee:
    def __init__(self, emp_id, name, salary, department):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary
        self.department = department

    def calculate_overtime(self, hours, rate_per_hour):
        return hours * rate_per_hour

e1 = Employee(1, "Giri", 40000, "HR")
print("Overtime pay:", e1.calculate_overtime(5, 200))


numbers = [2, 3, 4]
total = sum(numbers)

product = 1
for num in numbers:
    product *= num

print("Sum:", total)
print("Product:", product)


text = "Madhansai"
reversed_text = text[::-1]
print("Reversed string:", reversed_text)









































