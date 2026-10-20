def notas(*notas):
    qtd_notas = media = 0

    for i in notas:
        teste = 0
        if i == True:
            teste = 1
        else:
            qtd_notas += 1
            if qtd_notas == 1:
                maior_nota = i
                menor_nota = i
            elif maior_nota < i:
                maior_nota = i
            elif menor_nota > i:
                menor_nota = i
            else:
                pass
        media += i
    media = media / qtd_notas

    alunos = {"Total" : qtd_notas, "Maior" : maior_nota, "Menor" : menor_nota, "Média" : media}
    if teste == 1 and media >= 6:
        alunos["Situação"] = "Boa"
    elif teste == 1 and media < 6:
        alunos["Situação"] = "Ruim"
    else:
        pass

    return alunos


teste = True
resposta = notas(5,6,8,5,6,2,10,teste)
print(resposta)