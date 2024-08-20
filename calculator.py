# def add(x, y):
#     return x + y

# def subtract(x, y):
#     return x - y

# def multiply(x, y):
#     return x * y

# def divide(x, y):
#     if y == 0:
#         return "Error! Division by zero."
#     else:
#         return x / y

# def calculate():
#     try:
#         num1 = float(input("Enter first number: "))
#         operator = input("Enter operator (+, -, *, /): ")
#         num2 = float(input("Enter second number: "))
#     except ValueError:
#         print("Invalid input. Please enter numeric values.")
#         return

#     operations = {
#         '+': add,
#         '-': subtract,
#         '*': multiply,
#         '/': divide
#     }

#     if operator in operations:
#         result = operations[operator](num1, num2)
#         print(f"The result is: {result}")
#     else:
#         print("Invalid operator. Please enter one of +, -, *, /.")

# if __name__ == "__main__":
#     calculate()

def add(number1,number2):
    return (number1+number2)

def sub(number1,number2):
    return (number1-number2)

def mul(number1,number2):
    return (number1*number2)

def div(number1,number2):
    return (number1/number2)

select=int(input("Enter 1 for add \n 2 for sub \n 3 for mul \n 4 for div\n "))
number1=float(input("Enter the frist number:"))
number2=float(input("Enter the second number:"))

if select==1:
    print(number1 ,"+",number2 ,"=",add(number1,number2))
elif select==2:
    print(number1 ,"-",number2,"=" ,sub(number1,number2))
elif select==3:
    print(number1 ,"*",number2,"=" ,mul(number1,number2))
elif select==4:
    print(number1 ,"/",number2,"=" ,div(number1,number2))
else:
    print("invalid data")