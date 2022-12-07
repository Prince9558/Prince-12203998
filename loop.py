# Write a program to print numbers from one to ten using the while loop.

'''a=1
while a<=10:
    print(a)
    a=a+1

#Write a program to add 10 consecutive numbers starting from 1 using the while loop.
count=0
sum=0
while count<=10:
    sum=sum+count
    count=count+1
print("Sum of first 10 numbers: ",sum)

#Write a program to find the sum of the digits of a given number.
a=int(input("Please enter the number: "))
b=a
sum=0
rem=0
while a>0:
    rem=a%10
    a=a//10
    sum=sum+rem
print(sum)

# Write a program to display the reverse of the number entered.
num=int(input("Please enter the number: "))
x=num
rev=0
while num>0:
    rem=num%10
    num=num//10
    rev=rev*10+rem
print("Reverse of entered number is: ",rev) 

# Write a program to print the sum of the numbers from from 1 to 20 that are divisible by 5 using the while loop
count=1
sum=0
while count<=20:
    if count%5==0:
        sum=sum+count
    count=count+1
print("The sum of Numbers from 1 to 20 divisible by 5 is: ",sum)

#Write a program using the while loop to print the factorial of a number.
num=int(input("Enter the number: "))
fact=1
ans=1
while fact<=num:
    ans=ans*fact
    fact=fact+1
print(ans)

#Write a program to check whether the number entered is an Armstrong number or not.
num=int(input("Enter the number: "))
sum=0
x=num
while num>0:
    d=num%10
    num=num//10
    sum=sum+(d*d*d)
if (x==sum):
    print("The number",x,"is Armstrong Number")
else:
    print("The number",x,"is not Armstrong Number")

#RANGE
a=list(range(1,6))
b=list(range(1,20,2))
print(a)
print(b)

c=list(range(0,1))
d=list(range(1,1))
e=list(range(0))
print(c)
print(d)
print(e)'''

import random
a=int(input())
b=int(input())
c=random.randint(a,b)
print(c,"is randomly picked number")
if c>0:
    print("positive number")
else:
    print("negative number")
if c%2==0:
    print("even number")
else:
    print("odd number")
d=0
for i in range(1,b+1):
    if c%i==0:
        d=d+1
    else:
        continue
if d==2:
    print("prime number")
else:
    print("composite number")








