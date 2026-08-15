valor_saque = int(input('Digite o valor que deseja sacar: '))
total_saque = valor_saque

cedulas = [100, 50, 20, 10, 1]
notas = [0,0,0,0,0]
print(f'Você sacou {total_saque} Reais')

for i, cedula in enumerate(cedulas):
    if valor_saque >= cedula:
        notas[i] = valor_saque // cedula
        valor_saque = valor_saque % cedula
        print(end= '')
        print(f'{notas[i]} Nota(s) de {cedula}')
