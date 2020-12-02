#TASK-10:



#1)Write a Python program for all the cases which can check a string contains only a certain set of characters (in this case a-z, A-Z and 0-9).
def check(test_str):
    import re
    pattern = r'[a-zA-Z0-9.]'
    if re.search(pattern, test_str):
        print('valid')
    else:
        print('Invalid')

check(test_str='raghavi94')

#2)Write a Python program that matches a word containing 'ab'.
import re
txt="abrakadabra"
if re.search("ab",txt):
    print('Matched')
else:
    print('Not matched')

#3)Write a Python program to check for a number at the end of a word/sentence.
import re
string="BestEnlistDay10"
pattern='(\d+)$'
x=re.search(pattern,string)
if x:
    print('String ends with a number')
else:
    print('String does not end with a number')

#4)Write a Python program to search the numbers (0-9) of length between 1 to 3 in a given string

import re
results = re.finditer(r"([0-9]{1,3})", "123 456 789")
print("Number of length 1 to 3")
for i in results:
     print(i.group(0))


#5)Write a Python program to match a string that contains only uppercase letters

import re
string=str(input('Enter valid string'))
pattern='^[A-Z]+$'
if re.search(pattern,string):
    print('Valid string')
else:
    print('Invalid string')
               
