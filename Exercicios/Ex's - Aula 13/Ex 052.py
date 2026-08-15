print('Identificador de números primos')

num = int(input('Digite um número:'))
if num == 2:
    print('O 2 é Primo!')
elif num <= 1:
    print(f'O {num} não é Primo')
else:
    for c in range(2,num):
        teste = num % c
        if teste == 0:
            print(f'O {num} não é número primo')
            break
        if c == num-1:
            print(f'O {num} é um número primo!')


