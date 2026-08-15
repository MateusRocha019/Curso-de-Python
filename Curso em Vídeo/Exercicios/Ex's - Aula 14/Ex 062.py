termo = int(input('Digite o valor do primeiro termo: '))
razao = int(input('Digite o valor da razão: '))
contador = 1
soma = termo
confirmar = "S"
contador_max = 10
print(termo, end=' ')
while contador != contador_max:
    soma += razao
    contador += 1
    print(soma, end=' ')
print('\n')
while confirmar == 'S' or confirmar == 's':

    confirmar = input('\nQuer continuar a sequencia dos termos digite (S/N): ')

    if confirmar == 'S' or confirmar == 's':
        contador_max += int(input('\nDigite quantos termos a mais você quer ver: '))
        while contador != contador_max:
            soma += razao
            contador += 1
            print(soma, end=' ')
print(f'O total de termos foi: {contador}')