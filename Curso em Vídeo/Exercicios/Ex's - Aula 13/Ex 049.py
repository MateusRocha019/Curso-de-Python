print('='* 20 + ' Tabuada ' + '=' * 20 + '\n')
num = int(input('Digite o número que deseja ver a tabuada:'))

for c in range(1, 11,1):
    resultado = num * c
    print(f'{num} * {c} = {resultado}')
