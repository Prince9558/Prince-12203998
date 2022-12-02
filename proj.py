import random
a=int(input("enter starting range:- "))
b=int(input("enter ending range:- "))
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
