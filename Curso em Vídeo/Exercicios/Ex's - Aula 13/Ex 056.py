
lista_nome = []
lista_idade = []
lista_sexo = []
pessoas = 3
media = 0
idade_homem_mais_velho = 0
total_mulheres = 0
nome_homem_mais_velho = ""

for c in range(0, pessoas):
    nome = input(f'Digite o nome da {c+1}º pessoa: ')
    lista_nome.append(nome)

    idade = int(input(f'Digite a idade da {c+1}º pessoa: '))
    lista_idade.append(idade)

    sexo = input(f'Digite (f) para feminino ou (m) para masculino referente à {c+1}º pessoa: ').lower()
    lista_sexo.append(sexo)

for c in range(0, pessoas):
    media = media + lista_idade[c]
media = media / pessoas

for c in range(0, pessoas):
    if lista_sexo[c] == "m":
        if lista_idade[c] > idade_homem_mais_velho:
            idade_homem_mais_velho = lista_idade[c]
            nome_homem_mais_velho = lista_nome[c]

for c in range(0, pessoas):
    if lista_sexo[c] == "f":
        if lista_idade[c] < 20:
            total_mulheres += 1

print(f'A média de idade do grupo é: {media:.1f}')
print(f'O nome do homem mais velho é: {nome_homem_mais_velho}')
print(f'O total de mulheres abaixo de 20 anos é: {total_mulheres}')