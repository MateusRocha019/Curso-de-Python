jogadores = []
jogador = {}
gols_total = 0

print("-=" * 30)
while True:
    jogador["Nome"] = input("Digite o nome do jogador: ")
    jogador["Partidas jogadas"] = int(input("Digite quantas partidas o jogador jogou nessa temporada: "))

    for i in range(1, jogador["Partidas jogadas"]+1):
        jogador[f"Gols na {i}º Partida"] = int(input(f"Digite quantos gols ele fez na {i}ºPartida: "))
        gols_total += jogador[f"Gols na {i}º Partida"]
    jogador["Total de Gols"] = gols_total
    jogadores.append(jogador.copy())
    gols_total = 0
    resp = input("Deseja adicionar outro jogador? [S/N] : ").strip().upper()[0]
    print("-=" * 30)
    if resp in "N":
        break

for k in jogadores:
    print(f"O jogador {k['Nome']} jogou {k['Partidas jogadas']} partidas e fez {k['Total de Gols']} Gols no campeonato")
print("-=" * 30)