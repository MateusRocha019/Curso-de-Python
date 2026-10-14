import time
import random
jogadores = {}
tempo = 0.4
for i in range(1,5):
    print(f"O jogador {i} está jogando os dados...")

    jogadores[f"Jogador {i}"] = random.randint(1,6)
    time.sleep(tempo)
    print(f'3...')
    time.sleep(tempo)
    print(f'2...')
    time.sleep(tempo)
    print(f'1...')
    time.sleep(tempo)
    print(f'O jogador {i} tirou {jogadores[f"Jogador {i}"]} \n')
dict_ordenado = dict(sorted(jogadores.items(), key=lambda item: item[1]))

for k, v in dict_ordenado.items():
    print(f"O {k} tirou {v}")
    vencedor = k
    pontuação = v

print(f'\nO vencedor foi o {vencedor} e pontuou {pontuação}')