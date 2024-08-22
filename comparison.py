num1 = int(input('number1 =>>> '))
num2 = int(input('number2 =>>> '))
num3 = int(input('number3 =>>> '))

def comparison (n1,n2,n3):
    if num1 > num2 and num1>num3:
        print('Number 1 is bigger than number 2 and number 3')
    elif num2 > num1 and num2>num3:
        print('Number 2 is bigger than number 1 and number 3')
    else:
        print('Number 3 is bigger than number 1 and number 2')

comparison(num1,num2,num3)