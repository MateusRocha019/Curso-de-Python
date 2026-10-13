# matriz = [[],[],[]],[[],[],[]],[[],[],[]]
matriz = [[0 for _ in range(3)] for _ in range(3)]
soma_pares_total = soma_valor_col_3 = maior_valor_linha_2 = 0

for i in range(0,3):
    for j in range(0,3):
        matriz[i][j] = int(input(f"Digite o valor para a posição ({i},{j}): "))
        if matriz[i][j] % 2 == 0:
            soma_pares_total += matriz[i][j]
        if j == 2:
            soma_valor_col_3 += matriz[i][j]
        if i == 1:
            if j == 0 or maior_valor_linha_2 < matriz[i][j]:
                maior_valor_linha_2 = matriz[i][j]
            else:
                pass


for i in range(0,3):
    print(matriz[i])

print(f'A soma de número pares é {soma_pares_total}')
print(f'O total somado na coluna 3 é: {soma_valor_col_3}')
print(f'O maior valor da linha 2 é: {maior_valor_linha_2}')