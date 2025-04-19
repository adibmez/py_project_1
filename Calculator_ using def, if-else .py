'''Simple def, if-else Function Calc'''

print("Welcome to Simple Calculator!")
def calculator():
    n1 = float(input('Please input first integer: '))
    op = input('Operator (+,-,*,/) : ')
    n2 = float(input('then type operational integer: '))

    if op == '+':
        result = n1+n2
    elif op == '-':
        result = n1-n2
    elif op == '*':
        result = n1*n2
    elif op == '/':
        if n2 == 0:
            print('Cannot be divided by zero!!')
            return
        else:
            result = (n1/n2)
    else:
        print('Math Error!')
        return

    print(result)

calculator()
print('--- This is my calculator ---')
