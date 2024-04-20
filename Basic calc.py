num1 = int(input('Enter the first number: '))
num2 = int(input('Enter the second number: '))
op = input('Enter the Operator: ')

if op == '+':
    print('The addition is',num1+num2)
elif op == '-':
    print('The subtraction is',num1-num2)
elif op == '*':
    print('The mulitiplicaiton is',num1*num2)
elif op == '/':
    print('The division is',num1/num2)
else:
    print('Invalid operator')