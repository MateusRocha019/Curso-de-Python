from random import randint
lista = []
for c in range(0,5):
    num_aleatorio = randint(0,100)
    lista.append(num_aleatorio)
tupla = ()
tupla = lista
print(f'O número gerados na Tupla são: {tupla}')

maior_numero = menor_numero = cont = 0

for c in tupla:
    if cont == 0:
        maior_numero = c
        menor_numero = c
        cont += 1
    if c > maior_numero:
        maior_numero = c
    if c < menor_numero:
        menor_numero = c

print(f'O maior número na tupla é: {maior_numero}')
print(f'O menor número na tupla é: {menor_numero}')