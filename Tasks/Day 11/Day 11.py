#TASK-11:

#filter,zip,reduce,lambda:

#1)Write a program using zip() function and list() function, create a merged list of tuples from the two lists given.
a=[1,2,3]
b=[4,5,6]
print(list(zip(a,b)))

#2)First create a range from 1 to 8. Then using zip, merge the given list and the range together to create a new list of tuples.
r=[2,4,6,8,10,12,14,16]
s=[i for i in range(1,9)]
print(list(zip(s,r)))

#3)Using sorted() function, sort the list in ascending order.
l1=[2,1,4,3,7,5,6]
x=sorted(l1)
print('Sorted list:',x)

#4)Write a program using filter function, filter the even numbers so that only odd numbers are passed to the new list.

l2=[1,2,3,4,5,6,7,8]
print(list(filter(lambda x:x%2,l2)))


#Definitions:
#Lambda:

#Lambda is an anonumous function temporarily used instead of regular function.
#It can take any no of arguments but only one expression
#Syntax:
#arguments:expression

#Filter:
#Syntax:
#filter(function,sequence/iterable)
#function	A Function to be run for each item in the iterable
#iterable	The iterable to be filtered
   
#Map:
#Syntax:
#map(function,iterable)
#The difference between filter and map is that in filter in place of function,there will be a condition which must be satisfied for iterable to be filtered.
#In map,function part will execute since it has the expression.

#Eg:
#filter(lambda x:x%2==0,list)-->here even condn. shld be satisfied for execution.
#map(lambda x:x+2,list)-->here it just adds 2 to list ,there is no condn. here.

#zip
#eg:
#a=[1,2]
#b=[3,4]
#zip(a,b)-->outputs [(1,3),(2,4)]-->it pairs up 1st and 2nd elements of 2 list and returns tuples of lists.
