#TASK 3:

#1)Write a Python script to merge two Python dictionaries

d1={'Ram':18,'Ravi':20}
d2={'Ravi':22,'Sita':24}
d3=d1.update(d2)
print(d3)

#2)Write a Python program to remove a key from a dictionary

print(d1)
d1.pop('Ravi')
print(d1)

#3)Write a Python program to map two lists into a dictionary

l1=['a','b','c']
l2=[1,2,3]
l3=dict(zip(l1,l2))
print(l3)

#4)Write a Python program to find the length of a set

set1={'Apple','Banana','Orange'}
print(len(set1))

#5)Write a Python program to remove the intersection of a 2nd set from the 1st set

set2={'Rose','Lily','Jasmine'}
set3={'Lily','Lotus','Hibiscus'}
print(set2-set3)


    


