num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))

if num1 > num2:
    print(f'O primeiro número é maior: {num1}')
elif num1 < num2:
    print(f'O segundo número é maior: {num2}')
else:
    print(f'Os número são iguais {num1} = {num2}')
