#TASK 6:

#1)Write a program to loop through a list of numbers and add +2 to every value to elements in list

list1=[1,2,3,4,5]
for i in list1:
    i+=2
    print(i)

#2)
""" Write a program to get the below pattern
54321
4321
321
21
1 """

print("-------------------")
    

for i in range(5,0,-1):
  print("".join(format(j)   for j in range(i,0,-1)))    

#3)Python Program to Print the Fibonacci sequence

n=int(input('Enter n:'))
a=0
b=1
count=0
if(n<0):
    print('Enter +ve no')
else:

    print('Fibonacci series:')
    while(count<n):
        print(a)
        s=a+b
        a=b
        b=s
        count+=1

#4)Explain Armstrong number and write a code with a function

def amstrong(num) :
    """ It checks whether the given number is amstrong or not
        Amstrong:Sum of (order of n) of each digit is equal to the number itself
        eg:153=1^3 + 5^3 + 3^3 """
    sum = 0
    temp = num
    order=len(str(num))
    while num > 0 :
        r = num % 10
        sum += r ** order
        num //= 10

    if sum == temp :
        print(f"{sum} is Amstrong Number")
    else :
        print("Number is not  Amstrong Number")


num = int(input("Enter the number (Amstrong):"))
amstrong(num) #Amstrong function is called


#5)Write a program to print the multiplication table of 9
n=int(input('Enter n:'))
m=int(input('Enter the factor upto which the table is to be printed:'))
if(n>0):
    for i in range(1,m+1):
        print(n*i)

#6)Check if a program is negative or positive
n=int(input('Enter n:'))
if(n>0):
    print('The number is positive')
elif n==0:
    print('Number is 0')
else:
    print('The number is negative')

#7)Write a program to convert the number of days to years

days=int(input('Enter no.of days:'))
year=int(days/365)
print('Year=',year)

#8)Solve Trigonometry problem using math function write a program to solve using math function
    
import math as m
a=m.sin(1/2)
b=m.cos(1/2)
sum=round(a+b)
print("Trignometry problem=",sum)

#9)Create a calculator only on a code level by using if condition (Basic arithmetic calculation)
n1=int(input('Enter num1:'))
n2=int(input('Enter num2:'))
o=0
operator=input('Enter operator:')
if(operator=='+'):
    o=n1+n2
if(operator=='-'):
    o=n1-n2
if(operator=='*'):
    o=n1*n2
if(operator=='/'):
    o=n1//n2
print('Result=',o)    

      
