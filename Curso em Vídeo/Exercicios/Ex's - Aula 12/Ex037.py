print('Conversor de inteiro para binário, octal ou hexadecimal.')

num = int(input('Digite um número inteiro: '))

print('\nPara converter para binário digite 1\nPara converter para octal digite 2\nPara converter para hexadecimal digite 3\n')
codigo = int(input('Digite o código da conversão: '))

if codigo == 1:
    print(f'Em Binário: {num:b}')
elif codigo == 2:
    print(f'Em Octal: {num:o}')
elif codigo == 3:
    print(f'Em Hexadecimal: {num:X}')
else:
    print('Você digitou o código errado, tente novamente!')
