def ficha(nome="Sem Nome", gols="Sem amostragem de gols"):
    print("-=" * 30)
    print(f"Jogador -> {nome}\nGols -> {gols}")
    print("-=" * 30)


nome = input("Digite o nome do jogador: ").strip()
gols = input("Digite a quantidade de gols que ele fez: ").strip()


if nome == "" and gols == "":
    ficha()
elif nome == "":
    ficha(gols=gols)
elif gols == "":
    ficha(nome=nome)
else:
    ficha(nome, gols)