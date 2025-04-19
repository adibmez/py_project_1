print('--- Welcome to my calculator ---')

n1 = float(input('Please input first integer: '))
op = input('Operator +,-,*,/ : ')
n2 = float(input('then type operational integer: '))

if op == '+':
    print(n1 + n2)
elif op == '-':
    print(n1 - n2)
elif op == '*':
    print(n1*n2)
elif op == '/':
    if n2 == 0:
        print('Cannot be devided by zero!!')
    else:
        print(n1/n2)
else:
    print('Math error!')

print('--- This is my calculator ---')
