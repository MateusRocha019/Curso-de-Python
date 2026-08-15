for c in range(1,6):
    peso = float(input(f'Digite o peso da {c}º pessoa: '))
    if c == 1:
        maior_peso = peso
        menor_peso = peso
    elif peso > maior_peso:
        maior_peso = peso
    elif peso < menor_peso:
        menor_peso = peso

print(f'O maior peso foi: {maior_peso}Kg')
print(f'O menor peso foi: {menor_peso}Kg')