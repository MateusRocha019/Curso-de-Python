from datetime import date

ano_atual = date.today().year

print('====== SAIBA A CATEGORIA DE COMPETIÇÃO PELO SEU ANO DE NASCIMENTO ======')

ano_nascimento = int(input('Digite o ano do seu nascimento: '))

idade_atual = ano_atual - ano_nascimento

if idade_atual <= 9:
    print('Você está na categoria MIRIM')
elif idade_atual <= 14:
    print('Você está na categoria INFANTIL')
elif idade_atual <= 19:
    print('Você está na categoria JUNIOR')
elif idade_atual <= 20:
    print('Você está na categoria SÊNIOR')
elif idade_atual > 20:
    print('Você está na categoria MASTER')
else:
    print('Ocorreu um erro, tente novamente!')

