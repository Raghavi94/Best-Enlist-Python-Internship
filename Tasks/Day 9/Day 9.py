#TASK-9:

#1)Create a lambda function that multiplies argument x with argument y
a=int(input('Enter a'))
b=int(input('Enter b'))
x=lambda a,b : a*b
print("Product is:",x(a,b))

#2)Write a Python program to create Fibonacci series to n using Lambda
from functools import reduce

fib = lambda n: reduce(lambda x, _: x+[x[-1]+x[-2]],range(n-2),[0,1]) 
n=int(input('Enter no of terms'))
print(fib(n)) 

#3)Write a Python program that multiply each number of given list with a given number

m=int(input('Enter the number which is to be multiplied with the elements of list'))
l1=[1,2,3]
print('Old list:',l1)
z=list(map(lambda a:a*m,l1))
print('New list:',z)

#4)Write a Python program to find numbers divisible by 9 from a list of numbers

l2=[1,3,4,6,8,9]
r=list(filter(lambda x:x%3==0,l2))
print('Numbers divisible by 3 are:',r)

#5)Write a Python program to count the even numbers in a given list of integers

l3=[1,2,3,4,5,6,7,8]
even=list(filter(lambda y:y%2==0,l3))
print('Even nos are:',even)
    
        

