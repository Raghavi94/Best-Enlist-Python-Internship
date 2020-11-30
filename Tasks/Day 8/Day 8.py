#TASK 8:

#1)List down all the error types and check all the errors using a python program for all errors

#Index error
#Name error
#zerodivision error

a=[0,1,2,3]
try:
    print(a[1])
    print(a[4],a[1]//0)
except(IndexError,ZeroDivisionError):
    print('Index error and zero division error occured')

#2)Design a simple calculator app with try and except for all use cases
import math  
while 1:  
    print ("1) Add")  
    print ("2) Subtract")
    print ("3) Divide")
    print ("4) Multiply")
    print ("0) Exit")

    try:  # This is a try statement used to handle errors
        answer = int(input("Option: "))  
        if answer == 1:  
            first = float(input("First Number: "))  
            second = float(input("Second Number: "))  
            final = first + second 
            print ("Answer:", float(final)) 
            print()
        elif answer == 2:
            first = float(input("First Number: "))
            second = float(input("Second Number: "))
            final = first - second
            print ("Answer:", float(final)) 
            print()
        elif answer == 3:
            first = float(input("First Number: "))
            second = float(input("Second Number: "))
            final = first / second
            print ("Answer:", float(final))
            print()
        elif answer == 4:
            first = float(input("First Number: "))
            second = float(input("Second Number: "))
            final = first * second
            print ("Answer:", float(final))
            print()
        elif answer == 0: 
            break
        else:  
            print ("\nPlease select a valid option number\n")
    except NameError: 
        
        print ("\nNameError: Please Use Numbers Only\n")
        
    except SyntaxError:  # SyntaxError means we typed letters or special characters i.e !@#$%^&*( or if we tried to run python code
        
        print ("\nSyntaxError: Please Use Numbers Only\n")
        
    except TypeError:  # TypeError is if we entered letters and special characters or tried to run python code
        
        print ("\nTypeError: Please Use Numbers Only\n")
        
    except AttributeError:  # AttributeError handles rare occurances in the code where numbers not on the list are handled outside of the if statement
        
        print ("\nAttributeError: Please Use Numbers Only\n")
       


#3)print one message if the try block raises a NameError and another for other errors

try:
    print(x)
except NameError:
    print('NameError:x is not defined')


#4)When try-except scenario is not required?

#try-except is used for checking and validation purpose,otherwise it is not needed

#5)Try getting an input inside the try catch block

try:
    n=int(input('Enter a number'))
    print('Input you gave is valid')
except ValueError:
    print('Invalid input')
    
    
    

    
