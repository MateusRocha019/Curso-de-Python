mulheres = homens = pessoas = 0
while True:
    idade = int(input('Digite a idade da pessoa: '))
    sexo = str(input('Digite o sexo da pessoa (M/F): ')).strip().upper()
    validacao = str(input('Se deseja adicionar mais alguém digite S ou se não deseja digite N: ')).strip().upper()
    if idade > 18:
        pessoas += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulheres += 1
    if validacao == 'N' or validacao == 'NÃO' or validacao == 'NAO':
        break

print(f'\nForam cadastrados {pessoas} pessoas com mais de 18 anos')
print(f'Foram cadastrados {homens} homens')
print(f'Foram cadastradas {mulheres} mulheres com menos de 20 anos')