total_produtos_mais_1000 = total_gasto = contador_produtos = valor_produto_mais_barato = 0
nome_produto_mais_barato = ''


while True:
    nome = str(input('Digite o nome do produto: '))
    preco = float(input('Digite o preço do produto: '))

    if contador_produtos == 0:
        contador_produtos += 1
        nome_produto_mais_barato = nome
        valor_produto_mais_barato = preco

    if preco < valor_produto_mais_barato:
        nome_produto_mais_barato = nome
        valor_produto_mais_barato = preco

    total_gasto += preco

    if preco > 1000:
        total_produtos_mais_1000 += 1

    test_continuacao = str(input('Digite (S) para adicionar mais um produto ou digite (N) para finalizar: ')).strip().upper()[0]
    if test_continuacao == 'N':
        break

print(f'O total gasto na compra foi de {total_gasto}')
if total_produtos_mais_1000 > 1 or total_produtos_mais_1000 == 0:
    print(f'{total_produtos_mais_1000} produtos custaram mais de 1000,00 Reais')
else:
    print(f'{total_produtos_mais_1000} produto custou mais de 1000,00 Reais')
print(f'O nome do produto mais barato é {nome_produto_mais_barato} e custou {valor_produto_mais_barato}')