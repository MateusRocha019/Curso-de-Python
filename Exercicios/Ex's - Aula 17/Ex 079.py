
lista = []
i = "S"
while i == "S":

    num = int(input('\nDigite um valor: '))

    if num in lista:
        print('\nEsse número já encontra-se na lista! E por isso não foi adicionado!')
    else:
        lista.append(num)
    while True:
        i = str(input('\nDeseja adicionar outro número? (S/N) -> ')).strip().upper()[0:1]
        if i in "SN":
            break

lista.sort()
print(f'\nOs valores digitados em ordem crescente são {lista}')