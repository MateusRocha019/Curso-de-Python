valor_produto = float(input('Digite o valor do produto: '))

print('====== Escolha a forma de pagamento e digite o código referente a ela =======')

print('À vista dinheiro/cheque tem 10% de desconto -> Código 1')
print('À vista no cartão tem 5% de desconto -> Código 2')
print('Em até 2 Vezes no cartão, mesmo preço -> Código 3')
print('Em 3 Vezes ou mais tem 20% de juros -> Código 4')

codigo = int(input('Digite o número do código: '))

if codigo == 1:
    novo_valor = valor_produto - (valor_produto * 0.1)
    print(f'O valor do seu produto ficará {novo_valor:.2f} Reais')
elif codigo == 2:
    novo_valor = valor_produto - (valor_produto * 0.05)
    print(f'O valor do seu produto ficará {novo_valor:.2f} Reais')
elif codigo == 3:
    print(f'O valor do seu produto ficará {valor_produto:.2f} Reais')
elif codigo == 4:
    novo_valor = valor_produto + (valor_produto * 0.2)
    print(f'O valor do seu produto ficará {novo_valor:.2f} Reais')
else:
    print('Código Inválido. Digite o código novamente!')
