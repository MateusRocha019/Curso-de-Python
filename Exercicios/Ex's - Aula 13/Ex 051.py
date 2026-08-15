primeiro_termo = float(input('Digite o valor do primeiro termo: '))
razao = float(input('Digite o valor da razão de uma PA: '))

print('A sequencia da progressão aritmetica é: ')
soma = primeiro_termo

for c in range(0,10):
    print(f'{soma:.1f}', end=' ')
    soma += razao