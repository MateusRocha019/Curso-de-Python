num1 = float(input('Digite um número: '))
num2 = float(input('Digite outro número: '))
op = 0
while op != 5:
    print('\n[1] Somar\n[2] Multiplicar\n[3] Maior\n[4] Novos Números\n[5] Sair Programa\n')
    op = int(input('Selecione a operação desejada: ' ))

    if op == 1:
        soma = num1 + num2
        print(f'A soma de {num1:.1f} + {num2:.1f} = {soma:.1f}')
    elif op == 2:
        multi = num1 * num2
        print(f'A multiplicação de {num1:.1f} * {num2:.1f} = {multi:.1f}')
    elif op == 3:
        if num1 > num2:
            print(f'O número {num1:.1f} é maior que {num2:.1f}')
        else:
            print(f'O número {num1:.1f} não é maior que {num2:.1f}')
    elif op == 4:
        num1 = float(input('Digite um número: '))
        num2 = float(input('Digite outro número: '))