valor_saque = int(input('Digite o valor que deseja sacar: '))
total_saque = valor_saque

notas_50 = notas_20 = notas_10 = notas_1 = 0

if valor_saque >= 50:
    notas_50 = valor_saque // 50
    valor_saque = valor_saque % 50
if valor_saque >= 20:
    notas_20 = valor_saque // 20
    valor_saque = valor_saque % 20
if valor_saque >= 10:
    notas_10 = valor_saque // 10
    valor_saque = valor_saque % 10

notas_1 = valor_saque

print(f'Você sacou {total_saque}, {notas_50} Notas de 50, {notas_20} Notas de 20, {notas_10} Notas de 10, {notas_1} Notas de 1.')
