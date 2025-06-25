Simple Calculator – Python Mini Project
This is a simple command-line calculator built using Python. It allows users to perform basic arithmetic operations: addition, subtraction, multiplication, and division.

Features
Add two numbers
Subtract one number from another
Multiply two numbers
Divide one number by another (with zero-division check)

How It Works

When you run the program, it prompts the user to:
Choose an operation (Add, Subtract, Multiply, Divide)

Enter two numbers

The calculator performs the selected operation and displays the result

Code

print('what do you want to do?')
print('1. add')
print('2. subtract')
print('3. multiply')
print('4. divide')

choice = input('Enter choice (1/2/3/4): ')

num1 = float(input('Enter first number: '))
num2 = float(input('Enter second number: '))

def add(num1, num2):
    print(f'The sum of {num1} and {num2} is {num1 + num2}') 

def subtract(num1, num2):
    print(f'The difference of {num1} and {num2} is {num1 - num2}')         

def multiply(num1, num2):
    print(f'The product of {num1} and {num2} is {num1 * num2}')

def divide(num1, num2):
    if num2 == 0:
        print('Error! Division by zero.')
    else:
        print(f'The quotient of {num1} and {num2} is {num1 / num2}')

if choice == '1':
    add(num1, num2)
elif choice == '2':
    subtract(num1, num2)
elif choice == '3':
    multiply(num1, num2)    
elif choice == '4':
    divide(num1, num2)
else:   
    print('Invalid choice')


Getting Started
Make sure Python is installed on your system.

Save the code above in a file named calculator.py.

Run the program using: python calculator.py

Author -
Mohd Osaid - https://github.com/Osaidsk
