produtos = ('Feijão', 15,'Arroz', 35,'Batata Frita', 20, 'Pão de Alho', 15,'Macarrão', 20, 'Linguiça', 30,'Miojo', 5,'Kit Kat', 3.50)
calcular_tamanho_espaços = 0

print('-'*40)
print('LISTAGEM DE PREÇOS'.center(38))
print('-'*40)

for c in range(0,15,2):
    calcular_tamanho_espaços = len(produtos[c])
    valor_produto = produtos[c+1]

    print(produtos[c],'.'*(30-calcular_tamanho_espaços),f'R${valor_produto:.2f}')
print('-'*40)