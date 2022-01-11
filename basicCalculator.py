num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))
op = input('Enter Operator: ')

if op == "+":
    print(num1+num2)
elif op == "-":
    print(num1-num2)
elif op == "*":
    print(num1*num2)
elif op == "/":
    print(num1/num2)
else:
    print("You must enter a valid operator!")