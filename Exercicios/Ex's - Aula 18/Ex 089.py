aluno = []
dados = []

while True:
    dados.append(input("Digite o nome do Aluno: "))
    dados.append(float(input('Digite a Primeira Nota: ')))
    dados.append(float(input('Digite a Segunda Nota: ')))
    dados.append((dados[1]+dados[2])/2)
    aluno.append(dados[:])
    dados.clear()
    check = input("Deseja adicionar outro aluno? [S/N] ").upper().split()[0]
    if check in "Nn": break

print("-=" * 8 , "Média alunos" , "-=" * 8)
for i in range (0,len(aluno)):
    print(f'O Aluno {aluno[i][0]} ficou com média {aluno[i][3]}')

print()
print("-=" * 8 , "Lista de Alunos" , "-=" * 8)
while True:

    for i in range(0,len(aluno)):
        print(f"Aluno {aluno[i][0]} - Número: {i+1}")
    num_aluno = (int(input("\nSelecione o número do Aluno que deseja ver as notas: "))-1)
    print(f"\nO aluno {aluno[num_aluno][0]} tirou as notas {aluno[num_aluno][1]} e {aluno[num_aluno][2]}")

    check = input("\nDeseja ver as notas de outro aluno? ").upper().split()[0]
    if check in "Nn": break