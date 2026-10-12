# lista = [[3,1,5],[6,4,10]]
# lista[0].sort()
# lista[1].sort()
# print(lista)

lista = [[],[]]

for i in range(1,7):
    num = int(input(f'Digite o {i}º valor: '))
    if num % 2 == 0:
        lista[1].append(num)
    else:
        lista[0].append(num)

lista[0].sort()
lista[1].sort()

print(f"Os valores ímpares digitados foram {lista[0]}\nOs valores pares digitados foram {lista[1]}")