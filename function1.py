def display():
    print("Gangster coming soon")
display()

def print_msg():
    str1=input("Please Enter Your Name:")
    print("Dear",str1,"Welcome to Bihar")
print_msg()

#Write a program to add the sum of digits from 1 to 25,50 to 76 and 90 to 101 using three different for loop.
sum=0
for i in range(1,25):
    sum=sum+i
print(sum)

sum=0
for i in range(50,76):
    sum=sum+i
print(sum)

sum=0
for i in range(90,101):
    sum=sum+i
print(sum)

# now the above question can be solved by using function
def sum(x,y):
    s=0;
    for i in range(x,y+1):
        s=s+i
    print(s)
sum(1,24)
sum(50,75)
sum(90,100)

#Write a program to find the maximum of two numbers.
def printMax(num1,num2):
    print("num1: ",num1)
    print("num2: ",num2)
    if num1>num2:
        print(num1, "is greater than", num2)
    elif num1<num2:
        print(num2,"is greater than", num1)
    else:
        print("both numbers are equal")
printMax(20,10)
