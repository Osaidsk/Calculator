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
