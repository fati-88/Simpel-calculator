number1 = int(input('Hello user! Enter the first number: ')) 
number2 = int(input('Okay, enter the second one: ')) 
operation = input('What is the math operation? (+, -, *, /): ')

if operation == '+':
     print(number1 + number2) 
elif operation == '-': 
    print(number1 - number2) 
elif operation == '*': 
    print(number1 * number2) 
elif operation == '/': 
    print(number1/number2)
if number2 != 0: 
    print(number1 / number2) 
else: 
    print("Error: Ca#ffffffnnot divide by zero!") 