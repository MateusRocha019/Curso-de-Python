
lista = []

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

print(f'O total de números digitados foi: {len(lista)}')
lista.sort(reverse=True)
print(f'A lista na ordem decrescente: {lista}')

if 5 in lista:
    print('O valor 5 está na lista!')
else:
    print('O valor 5 não foi encontrado na lista!')