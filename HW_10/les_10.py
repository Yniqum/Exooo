"""
Calculator
------------------------------------------------------------------
This calculator can perform the following mathematical operations
'+'
'-'
'*'
'/'
"""


def addition(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


print("specify operation.")
print("1.addition")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
while True:
    choice = input("Enter your choice(1/2/3/4): ")
    if choice in ('1', '2', '3', '4'):
        try:
            number1 = float(input("Enter first number: "))
        except ValueError:
            print("you didn't enter a number")
            continue
        try:
            number2 = float(input("Enter second number: "))
        except ValueError:
            print("you didn't enter a number")
            continue
        if choice == '1':
            print(number1, "+", number2, "=", addition(number1, number2))
        elif choice == '2':
            print(number1, "-", number2, "=", subtract(number1, number2))
        elif choice == '3':
            print(number1, "*", number2, "=", multiply(number1, number2))
        elif choice == '4':
            try:
                print(number1, "/", number2, "=", divide(number1, number2))
            except ZeroDivisionError:
                print('it is not divisible by zero')
                continue
        break
    else:
        print("Entered input is invalid")
