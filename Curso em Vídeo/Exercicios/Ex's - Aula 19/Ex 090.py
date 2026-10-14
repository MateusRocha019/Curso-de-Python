aluno = {}
aluno["nome"] = input('Digite o nome do aluno: ')
aluno['média'] = float(input('Digite a média do aluno: '))

if aluno['média'] >= 7:
    aluno['situação'] = "Aprovado"
else:
    aluno['situação'] = "Reprovado"

print(f'O {aluno["nome"]} ficou com média {aluno["média"]} e sua situação é {aluno["situação"]}!')