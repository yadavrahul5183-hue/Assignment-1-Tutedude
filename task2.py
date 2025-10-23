'''
Task 2: Create a Personalized Greeting
Problem Statement: Write a Python program that:
1.  Takes a user's first name and last name as input.
2.  Concatenates the first name and last name into a full name.
3.  Prints a personalized greeting message using the full name.
'''

#Solution

Fname= input("Enter your first name:")
Fname= str(Fname)
Lname= input("Enter your last name:")
Lname= str(Lname)

welcome_message= "Hello, " + Fname + " " + Lname +"! Welcome to my sacred domain."

print(welcome_message)