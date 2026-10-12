import random
import time

lista_de_jogos = []
jogos = []

num_jogos = int(input("Digite o número de jogos de deseja criar: "))
print()
for i in range(0,num_jogos):

    jogos = random.sample(range(1,60),6)
    lista_de_jogos.append(jogos[:])
    jogos.clear()
    print(f"Jogo {i+1}: {lista_de_jogos[i]}")
    time.sleep(0.8)

print()
print( "=-" * 6 ,"BOA SORTE", "-=" * 6)