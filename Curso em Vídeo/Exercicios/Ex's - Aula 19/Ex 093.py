jogador = {}
gols_total = 0
jogador["Nome"] = input("Digite o nome do jogador: ")
jogador["Partidas jogadas"] = int(input("Digite quantas partidas o jogador jogou nessa temporada: "))

for i in range(1, jogador["Partidas jogadas"]+1):
    jogador[f"Gols na {i}º Partida"] = int(input(f"Digite quantos gols ele fez na {i}ºPartida: "))
    gols_total += jogador[f"Gols na {i}º Partida"]
jogador["Total de Gols"] = gols_total

print("-=" * 30)
print(jogador)
print("-=" * 30)

for k, v in jogador.items():
    print(f"{k} - {v}")