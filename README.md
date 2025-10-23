# Assignment-1-Tutedude
first assignment of tute dude
Task 1 Code Functionality: Simple Python Calculator

This Python script performs basic arithmetic operations on two numbers provided by the user. Its function is straightforward: it takes user input, converts it to a number format it can calculate with, and then displays the results of four operations.

1. The Input Phase: Asking for Numbers
The first four lines handleuser:
a = input("Enter your first number:")
a = float(a)
b = input("Enter your second number:")
b = float(b)

-The code pauses and waits for the user to type in their first number.

-Crucially, it immediately uses float() to convert that input into a decimal number (like 5.0 or 10.5). This ensures the program can handle both whole numbers and numbers with decimal points.

-It repeats the same process for the second number.

2. The Calculation Phase: Doing the Math
The next section takes the two numbers, a and b, and performs all four core operations at once, storing each result in its own variable:
add = a + b    # Adds the numbers
sub = a - b    # Subtracts the numbers
mul = a * b    # Multiplies the numbers
div = a / b    # Divides the numbers

3. The Output Phase: Showing the Results
Finally, the code displays the results neatly on the screen:
print("Addition:", add)
# ...and so on for Subtraction, Multiplication, and Division.
It uses the print() function to show a label (like "Addition:") followed by the calculated result for each operation.



Task 2 Functionality: Personalized Greeting Script
This Python script is designed to create a welcoming, customized message for the user by incorporating their full name. It showcases basic principles of user input and string manipulation.

1. The Input Phase: Gathering the User's Name
The first four lines of code are dedicated to asking the user for their information and storing it:
Fname = input("Enter your first name:")
Fname = str(Fname)
Lname = input("Enter your last name:")
Lname = str(Lname)

-The code uses the input() function, which pauses the program and waits for the user to type in their first name and then their last name.

-The str() function is used to explicitly confirm that the data entered is stored as a string (a sequence of characters/text), though input() does this by default in Python 3. This ensures the names can be correctly joined together later.

2. The Processing Phase: Building the Message
Next, the script combines the fixed text of the greeting with the user's input:
welcome_message = "Hello, " + Fname + " " + Lname + "!" + " Welcome to my sacred domain."

-This process is called string concatenation, where the + operator is used to literally glue different pieces of text together.

-It takes the greeting, adds the first name, adds a space, adds the last name, and finally adds the personalized welcome phrase to create one complete message.

3. The Output Phase: Displaying the Greeting
The final line displays the beautifully constructed message to the user:
print(welcome_message)

-The print() function simply takes the complete welcome_message variable and displays it on the screen, creating a personalized and engaging interaction.


