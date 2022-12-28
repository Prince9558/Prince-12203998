# Use for loop to print numbers from 1 to 5.
'''for i in range(1,6):
    print(i)

#Display capital letters from A to Z.
for i in range(65,91,1):
    print(chr(i),end=" ")

#Use for loop to print numbers from 1 to 10 in reverse order.
for i in range(10,0,-1):
    print(i,end=" ")

#Write a program to print squares of the first five numbers.
for i in range(1,6):
    b=i*i
    print(b,end=" ")

#Write a program to print even numbers from 0 to 10 and find their sum.
sum=0
for i in range(0,11,1):
    if i%2==0:
        print(i)
        sum=sum+i
print("Sum of Even numbers from 0 to 10 is: ",sum)

#Write a program to calculate the sum of numbers from 1 to 20 which are not divisible 2 , 3 or 5. 
sum=0
for i in range(1,20):
    if i%2==0 or i%3==0 or i%5==0:
        print("")
    else:
        print(i)
        sum=sum+i 

# Write a program that prompts a user to enter four numbers and find the greatest number among the four numbers entered.
a=int(input("Enter number: "))
b=int(input("Enter number: "))
c=int(input("Enter number: "))
d=int(input("Enter number: "))
sum=a+b+c+d
for i in range(sum):
    if i==a or i==b or i==c or i==d:
        large=i
print("Largest number: ",large)

# Write a program to generate a triangular number.
a=int(input("Enter number: "))
b=0
for i in range(a,0,-1):
    b=b+i
print(b)

# Write a program to display multiplication tables from 1 to 5.
for i in range(1,11,1):
    for j in range(1,6,1):
        print(format(i*j,"4d"),end=" ")
    print()

# Write a program to demonstrate the use of the break statement.
for i in range(1,100,1):
    if(i==11):
        break
    else:
        print("gangster")

#Check if the number entered is prime or not.else
num=int(input("Enter the number: "))
x=num
for i in range(2,num):
    if num%i==0:
        flag=0
        break
    else:
        flag=1
if (flag==1):
    print(num,"is prime ")
else:
    print(num,"is not prime ")'''

# Demonstrate the use of continue keyword
for i in range(1,11,1):
    if i == 5:
        continue
    print(i,end=" ")




                                                                                         