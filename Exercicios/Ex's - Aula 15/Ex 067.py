resultado = 0
while True:
    num = int(input('Digite um número para saber sua tabuada: '))
    print(f'Tabuada do número {num}')
    if num < 0:
        break
    for i in range(1, 11):
        resultado = num * i
        print(f'{num} X {i} = {resultado}')
    print('')