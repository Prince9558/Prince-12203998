'''a=str(input("str :"))
if a.startswith("Python") and a.endswith("programming"):
    print("valid")
else:
    print("invalid")

print("character with min val :",min(a))
print("character with max val :",max(a))

a=str(input("str: "))
if a.startswith("Python"):
    print("str is",a)
else:
    print("str after adding 'Python' :","python",a)

a=input("str: ")
n=" "
for i in a:
    m=i*2
    n=n+m
print(n)

a=input("str: ")
b=len(a)//2
if b==0:
    print("first half str of even length: ",a[:b])
else:
    print("second half str of odd length: ",a[b:])

print("Hello",end="")
print("World",end="")
print("Good Bye")

a=int(input("Length: "))
b=int(input("Breadth: "))
c=a*b
print("Area: ",c)

print("Enter integer number: ",end="")
num1=int(input())
print("Enter floating type number: ",end="")
num2=float(input())
print("number1: ",num1)
print("number2: ",num2)
c=num1+num2
print(c)

# Write a program to calculate the area of circle:
r=int(input("Radius: "))
pi=3.1428
Area=pi*r*r
print("Area of circle is: ",Area)

print(format(10.345,"10.2f"))
print(format(10,"10.2f"))
print(format(10.244556,"10.2f"))
print(format(10.234567,"<10.2f"))
print(format(0.31456,"10.2%"))
print(format(1.765,"10.2%"))
print(format(31.2345,"10.2e"))
print(format(131.2345,"10.2e"))'''

a=abs(-200)
print(a)
b=abs(45)
print(b)
c=max(10,20,30,40)
print(c)
e=max("brince","gangster","atul","28","14","5")
print(e)
f=pow(5,3)
print(f)
g=round(10.6454)
print(g)





