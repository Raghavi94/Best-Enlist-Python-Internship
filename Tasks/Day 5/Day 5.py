#TASK 5:

#1)Create a function getting two integer inputs from user. & print the following:

#Addition of two numbers is +value
#Subtraction of two numbers is +value
#Division of two numbers is +value
#Multiplication of two numbers is +value

def calci(a,b):
    print("Sum:",a+b)
    print("Difference:",a-b)
    print("Product:",a*b)
    print("Division:",a//b)
calci(10,5)

#2)Create a function covid( ) & it should accept patient name, and body temperature, by default the body temperature should be 98 degree

print("-----------------")

def covid(patient_name,body_temp='98 degree'):
    print("Patient name is " + patient_name)
    print("Body temperature is " + body_temp)
covid('Ravi')    

