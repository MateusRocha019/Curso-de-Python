lista = []
i = 1
cont = 0

num = int(input("Digite um número: "))
lista.append(num)
print(f'\nTamanho Lista {len(lista)}')
print(f'Itens lista: {lista}')

while i < 10:

    num = int(input("\nDigite um número: "))

    while True:
        if num < lista[cont]:
            lista.insert(cont, num)
            i += 1
            print(f'\nTamanho Lista {len(lista)}')
            print(f'Itens lista: {lista}')
            break
        elif num >= lista[cont] and cont+1 == len(lista):
            lista.append(num)
            print(f'\nTamanho Lista {len(lista)}')
            print(f'Itens lista: {lista}')
            i += 1
            break
        else:
            cont += 1
    cont = 0

print('\n', lista)




