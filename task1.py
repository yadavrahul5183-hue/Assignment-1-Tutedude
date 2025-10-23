'''
Task 1 : Perform Basic Mathematical Operations
Problem Statement: Write a python program that does the following :
1.  Takes two numbers as input from the user.
2.  Performs the basic mathematical operations on these two numbers:
o	Addition
o	Subtraction
o	Multiplication
o	Division
3.  Displays the results of each operation on the screen.
'''

#solution 

a= input("Enter your first number:")
a= float(a)
b= input("Enter your second number:")
b= float(b)

add= a + b
sub= a - b
mul= a * b
div= a / b

print("Addition:",add)
print("Subtraction:",sub)
print("Multiplication:",mul)
print("Division:",div)
