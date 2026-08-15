import random
vitorias_jogador = 0
print('JOGO DO PAR OU IMPAR')
while True:
    #Jogada Player
    num = int(input('Digite um número de 0 a 10: '))
    jogada_jogador = str(input('P -> Par ou I -> Impar. Digite uma opção: ')).strip().upper()

    #Jogada Maquina
    num_maquina = random.randint(0,10)

    #Teste vitória
    soma = num + num_maquina
    # Apresentação tela
    print(f'Você jogou {num} e o computador {num_maquina}. Total de {soma}', end=' ')
    if soma % 2 == 0:
        print('DEU PAR\n')
    else:
        print('DEU IMPAR\n')
    if (soma % 2 == 0 and jogada_jogador == 'P') or (soma % 2 != 0 and jogada_jogador == 'I'):
        vitorias_jogador += 1
        print('=' * 40)
        print('Você venceu jogue novamente!')
        print('=' * 40)
    else:
        print('='*40)
        print('Você perdeu!')
        print('=' * 40)
        break
print(f'Você venceu {vitorias_jogador} partidas seguidas da máquina!')
print('=' * 40)





