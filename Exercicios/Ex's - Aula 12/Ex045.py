import random

print('========== JOGO DO JOKENPÔ ==========\n')

print('Pedra - Digite 1\nPapel - Digite 2\nTesoura - Digite 3\n')

jogada_pessoa = int(input('Digite um dos códigos acima: '))

jogada_robo = random.randint(1, 3)


objeto = {
    1: 'Pedra',
    2: 'Papel',
    3: 'Tesoura'
}

if jogada_pessoa > 3 or jogada_pessoa < 1:
    print('Jogue novamente você digitou o código errado!')
elif jogada_pessoa == jogada_robo:
    print(f'Você jogou {objeto[jogada_pessoa]} e a Maquina {objeto[jogada_robo]}. Vocês Empataram!')
elif (jogada_pessoa == 3 and jogada_robo == 2) or (jogada_pessoa == 2 and jogada_robo == 1) or (jogada_pessoa == 1 and jogada_robo == 3):
    print(f'Você jogou {objeto[jogada_pessoa]} e a Maquina {objeto[jogada_robo]}. Você Ganhou!')
else:
    print(f'Você jogou {objeto[jogada_pessoa]} e a Maquina {objeto[jogada_robo]}. Você Perdeu!')