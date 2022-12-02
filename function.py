'''a="welcometopython"
b=a.isalpha()
c=a.isdigit()
d=a.isupper()
e=a.islower()
print(b)
print(c)
print(d)
print(e)

a="HELLO, bhai sahab"
t="12203998"
b=a.startswith("HELLO")
print(b)
c=a.endswith("sahab")
print(c)
print(t.find("2"))
print(t.rfind("9"))
print(a.title())
print(a.capitalize())


def my_function():
    print("gangster coming soon")
my_function()

def my_function(fname):
    print(fname + " Refsnes")

my_function("Email")
my_function("Tobias")
my_function("Linus")

def myfunction():
    pass

class MyClass:
    x=5
    
print(MyClass)

x=min(5,10,25)
y=max(5,10,25)
print(x)
print(y)

x=abs(-7.25)
print(x)

x=pow(4,3)
print(x)

import math
x=math.sqrt(64)    # return the square root of a number
print(x)

import math
x=math.ceil(1.4)  #returns the number upwards to its nearest integer
y=math.floor(1.4)   #returns the number downwards to its nearest integer
print(x)
print(y)

import math
x=math.pi
print(x)

def my_function():
    print("Hello world!")
my_function()

distinction_marks=75
a=int(input("marks: "))
if (a>distinction_marks):
    print("distinction")
else:
    print("not distinction")

a=int(input("num: "))
if a>0:
    print("positive")
elif a<0:
    print("negative")
elif a==0:
    print("zero")
else:
    print("GANGSTER")'''

list=["apple","banana","orange","12","100","guava","cherry"]
print()
'''print(list)
print(type(list))
for i in list:
    print(i,end="")
i=1
while i in list:
    print(i)
i=i+1
print(list[2:5])
print(list[:3])
print(list[::-1])
print(list[1:3:1])
print(len(list))
print(min(list))
print(max(list))

import random
random.shuffle(list)
print(list)

num=1
while (num<=5):
    print("num : %d" %num)
    num=num+1

a=input("Enter value: ")
b=a.swapcase()
print(b)
c=3*b
print(c)

a=input("Enter number: ")
c=0
for i in range(0,len(a),1):
    if a[i] =="0" or a[i]=="1":
        c=c+1
    else:
        c=c-1
if c==len(a):
    print(True)
else:
    print(False)

a=str(input())
c=""
d=""
e=""
for i in range(0,len(a),1):
    if a[i].isalpha():
        c=c+a[i]
    elif a[i].isdigit():
        d=d+a[i]
    else:
        e=e+a[i]
print("string: ",c)
print("digit: ",d)
print("character: ",e)

a=input("Enter value: ")
b=len(a)//2
c=a[0:b]
d=a[b:]
f=c[::-1]
g=d[::-1]
h=f+g
print(h)

class myclass:
    x=5

print(myclass)

class college:
    def student (self):
        self.name=input(" ")
        self.marks1=int(input(" "))
        self.marks2=int(input(" "))
    def display (self):
        print("name",self.name)
        print("marks of physics : ",self.marks1)
        print("marks of soft skill : ",self.marks2)
a=college()
a.student()
a.display()


class coll:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
p1=coll("sashank","100")
print(p1.name)
print(p1.marks)

class railway:
    def __init__(self,name,destiny):
        self.name=name
        self.destiny=destiny
p1=railway("sashank","lucknow")
print(p1.name)
print(p1.destiny)

class railway:
    def person (self):
        self.name=input(" ")
        self.destiny1=input(" ")
        self.destiny2=input(" ")
    def display (self):
        print("Enter your name : ",self.name)
        print("Boarding station : ",self.destiny1)
        print("destination: " , self.destiny2)
a=railway()
a.person()
a.display()

a= [1,2,5,3,8,3]
b=a.sorted()
print(a,type(a))

class railway:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return f"{self.name} :- {self.age}"
a=railway("Prince",15)
b=railway("Sashank",20)
c=railway("Anurag",21)
print(a)
print(b)
print(c)

class railway:
    def __init__(self,name,bp,dp):
        self.name=name
        self.bp=bp
        self.dp=dp
    def __str__(self):
        return f"{self.name} :- {self.bp} to {self.dp}"
a=railway("Gangster","phagwara","lucknow")
print(a)

class school:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __add__(self):
        print("My name is : "+self.name+"my age is"+self.age)
a=school("Prince",20)
print(a)'''
'''
a="prince raj"
x=len(a)-2
for i in range(0,x):
    print(a[i],end=" ")

a=input("hhh").split(',')
print(a)'''

'''for i in range(10):
    for j in range(i):
        print(j,end="")
    print()

for i in range(10):
    for j in range(i):
        print(i-1,end="")
    print()

a=10
b=5
a+=b
print(a)

a=input("enter:-").split(',')
for i in range(len(a)):
    a[i]=int(a[i])
print(a)

a=map(int,input("Enter:- ")).split(',')
print(a)

for i in range(10):
    for j in range(10,0,-1):
        print("*",end="")
    print()'''

'''for i in range(10):
    for j in range(0,10,1):
        print(j,end="")
    print()

class school:
    def __init__(self,f1,f2):
        self.f1=f1
        self.f2=f2
    def display(self):
        print(self.f1 ,self.f2)
class standard(school):
    pass
x=standard("hena",35)
x.display()

import random
a=int(input("enter starting range"))
b=int(input("enter ending range"))
c=random.randint(a,b)
print()
print(c,"is randomly picked number by computer")
print()
if c>0:
    print(c,"is a positive number")
else:
    print(c,"is a negative number")
if c%2==0:
    print(c,"is a even number ")
else:
    print(c,"is a odd number") 
d = 0
for i in range(1,b+1) :
    if c % i == 0:
        d = d + 1
    else:
        continue
if d == 2:
    print(c,"is a prime number")
else:
    print(c,"is a composite number")          
    
class A:
    def __init__(self,f1,f2):
        self.f1=f1
        self.f2=f2
    def display(self):
        print(self.f1,self.f2)
class B:
    def __init__(self,f1,f2):
        self.f1=f1
        self.f2=f2
    def display(self):
        print(self.f1,self.f2)
class C:
    def __init__(self,f1,f2):
        self.f1=f1
        self.f2=f2
    def display(self):
        print(self.f1,self.f2)
a=A("Sashank",20)
b=B("Anurag",22)
c=C("Prince",18)

a.display()
b.display()
c.display()

print(isinstance(a,A))
print(isinstance(b,B))
print(isinstance(c,C))

class school:
    def __init__(self,f1,f2):
        self.f1=f1
        self.f2=f2
    def __init__(self,f1,f2,f3):
        self.f1=f1
        self.f2=f2
        self.f3=f3
x=school("Gangster","Samastipur","Chhatauna")

a=input("keys: ").split(",")
v= input("Enter:-").split(',')
for i in range(len(v)):
    v[i] = int(v[i])
d=dict(zip(a,v))
print(d)
print(d.keys())
print(d.values())

a=tuple(map(int,input().split(",")))
c=[]
d={}
m = ()
print(type(c))
print(type(d))
print(type(m))
for i in a:
    if i not in c:
        b=a.count(i)
        d[i]=b
print(d)

a="Python"
print(a[-1::-3])
print(a[-1:-3])

a="Code tantra"
b=a[0:2]
c=a[-2:]
d=b+c
print(d)

a=str(input("enter:- "))
print(a[1:-1])

a="Active"
b=a[0]
c=a[-1]
d=a[1:-1]
e=c+d+b
print(b)
print(c)
print(d)
print(e)

a=input("enter:- ")
b=int(input("num: "))
c=a.remove(b)
d=print("output:",c)


a=str(input("str: "))
if len(a)>1:
    b=a[-1]+a[1:-1]+a[0]
    print(b)
elif len(a)==1:
    print(a)
else:
    print("null")

def display():
    print("Python")

display()

def display(x):
    print("python",x)

display(10)


a=str(input("str: "))
print(a*4)
b=a[::-1]
print(b*3)

a=str(input("str: "))
if len(a)>=3:
    b=a[0:3]
    print(b*3)
else:
    print(a)'''

str="Python provides built-in liabraries/nUsing python we can implement more and more applications/n/tPython is Robust"
print(str)
str="Hello/tpython/nPython is very interesting"
print(str)


