import random
tentativas = 0
num_jogador = 99
num_maquina = random.randint(1,10)
while num_maquina  != num_jogador:
    num_jogador = int(input('Advinhe o número que a máquina pensou de 1 a 10: '))
    tentativas += 1
print(f'Você digitou o número {num_jogador} e advinhou o número da maquina na {tentativas}º tentativa')
