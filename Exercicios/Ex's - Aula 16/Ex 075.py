quant_9 = cont = pos_first_3 = quant_num_pares = quant_num_3 = 0
lista = []

tupla = tuple(int(input('Digite um número: ')) for _ in range(5))

for c in tupla:
    if c == 9:
        quant_9 += 1
    if c % 2 == 0:
        lista.append(c)
        quant_num_pares += 1
    if c == 3 and pos_first_3 != 3:
        pos_first_3 = tupla.index(c)
        quant_num_3 += 1
    cont += 1


print(tupla)
if quant_9 == 1:
    print(f'O 9 Apaceceu: {quant_9} Vez')
else:
    print(f'O 9 Apaceceu: {quant_9} Vezes')

if quant_num_3 > 0:
    print(f'O primeiro 3 aparece na: {pos_first_3 + 1}º posição')
else:
    print('Não apareceu nenhum número 3 na tupla!')

if quant_num_pares > 0:
    print(f'A lista dos números pares foi: {lista}')
else:
    print('Não teve nenhum número par na tupla!')
