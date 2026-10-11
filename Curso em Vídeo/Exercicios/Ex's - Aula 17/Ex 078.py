i = 0
lista = []
for c in range(0,4):

    num = int(input('Digite um número: '))

    if i == 0:
        maior = menor = num
        i = 1
    if num > maior:
        maior = num
    if num < menor:
        menor = num

    lista.append(num)
print('')
for c , v in enumerate(lista):
    if v == maior:
        print(f'O maior valor é {maior} e foi encontrado na posição {c}.')
    if v == menor:
        print(f'O menor valor é {menor} e foi encontradonna posição {c}.')
