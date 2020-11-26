
#TASK 4:

#1)Write a program to create a list of n integer values and do the following

list1=[]
n=int(input('Enter n:'))
for i in range(1,n+1):
    list1.append(i)
print(list1)

#a)Add an item in to the list (using function)
list1.insert(1,4)#insert(index,number)
print(list1)

#b)Delete (using function)
del list1[1]
print(list1)

#c)Store the largest number from the list to a variable
a=max(list1)
print(a)


#d)Store the Smallest number from the list to a variable
b=min(list1)
print(b)



# 2) Create a tuple and print the reverse of the created tuple

t1=(1,2,3,4,5)
print(t1[::-1])

# 3) Create a tuple and convert tuple into list
print(list(t1))
