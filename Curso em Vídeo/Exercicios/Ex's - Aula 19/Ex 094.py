pessoas = []
pessoa_idade_acima_media = []
dados = {}
cont = 1
media_idade = qtd_mulheres = 0
while True:

    dados["Nome"] = input(f"Digite o nome da {cont}º pessoa: ")
    cont += 1
    dados["Sexo"] = input(f'Digite o sexo. Para Masculino -> M | Para Feminino -> F : ').strip().upper()[0]
    if dados["Sexo"] == "F":
        qtd_mulheres += 1
    dados["Idade"] = int(input('Digite a idade da pessoa: '))
    media_idade += dados['Idade']

    pessoas.append(dados.copy())


    resp = input("Deseja adicionar mais alguém? [S/N] : ").strip().upper()[0]
    if resp in "N":
        break
print("=-" * 30)

media_idade = media_idade / len(pessoas)
print(f"\nForam cadastradas um total de {len(pessoas)} pessoas.")
print(f'\nA média de idade das {len(pessoas)} pessoas da lista é {media_idade}')
print(f"\nNessa lista tem um total de {qtd_mulheres} Mulheres.")

for i in pessoas:
    if i["Idade"] > media_idade:
        pessoa_idade_acima_media.append(i['Idade'])

print(f'\nTem {len(pessoa_idade_acima_media)} pessoas com idades acima da média.')
print("=-" * 30)