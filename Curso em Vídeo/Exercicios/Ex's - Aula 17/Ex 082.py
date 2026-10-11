lista = []
listaImpar = []
listaPar = []

while True:

    lista.append(int(input("\nDigite um número: ")))
    while True:
        teste = input("\nDeseja continuar? (S/N) -> ").strip().upper()[0:1]
        if teste in "Nn":
            fim = 0
            break
        if teste in "Ss":
            fim = 1
            break
    if fim == 0:
        break

for c in range(0,len(lista)):
    print(lista[c])
    if (lista[c] % 2) == 0:
        listaPar.append(lista[c])
    else:
        listaImpar.append(lista[c])

print(f'\nA lista inicial era: {lista}')
print(f'\nA lista Par ficou: {listaPar}')
print(f'\nA lista Impar ficou: {listaImpar}')