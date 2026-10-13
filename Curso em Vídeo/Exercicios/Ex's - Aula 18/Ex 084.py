dados = []
pessoas = []
pessoas_mais_pesadas = []
pessoas_mais_leves = []

while True:

    dados.append(input('Digite o Nome: '))
    dados.append(float(input('Digite o peso: ')))

    pessoas.append(dados[:])
    dados.clear()

    while True:
        teste = input("Deseja adicionar outra pessoa? (S/N) ")[0].strip().upper()
        if teste in "SN":
            if teste in "S":
                break
            else:
                teste = "N"
                break
        else:
                print(f'Você digitou {teste} essa resposta não é válida tente novamente! ')
    if teste == 'N':
        break

print('-=' * 30)
print(f'Foram cadastradas um total de {len(pessoas)} pesssoas')

i = 0
for p in pessoas:
    if i == 0 or pessoas_mais_pesadas[0][1] == p[1]:
        pessoas_mais_pesadas.append(p[:])
        i += 1
    elif pessoas_mais_pesadas[0][1] < p[1]:
        pessoas_mais_pesadas.clear()
        pessoas_mais_pesadas.append(p[:])
    else:
        pass
print("\nÀs pessoas mais pessadas da lista são: ",end="" )
for p in pessoas_mais_pesadas:
    print(f"{p[0]} com {p[1]}Kg's", end="... ")

i = 0
for p in pessoas:
    if i == 0 or pessoas_mais_leves[0][1] == p[1]:
        pessoas_mais_leves.append(p[:])
        i += 1
    elif pessoas_mais_leves[0][1] > p[1]:
        pessoas_mais_leves.clear()
        pessoas_mais_leves.append(p[:])
    else:
        pass
print("\n\nÀs pessoas mais leves da lista são: ",end="" )
for p in pessoas_mais_leves:
    print(f"{p[0]} com {p[1]}Kg's", end="... ")
print('')
print('-=' * 30)