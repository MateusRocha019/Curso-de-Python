from datetime import date

hoje = date.today()
AnoAtual = hoje.year

AnoNascimento = int(input('Digite o ano do seu nascimento: '))

IdadeAtual = AnoAtual - AnoNascimento


if IdadeAtual < 18:
    TempoParaAlistar = 18 - IdadeAtual
    print(f'Faltam {TempoParaAlistar} Anos para você se alistar ')
elif IdadeAtual == 18:
    print(f'Você está no ano de fazer o Alistamento Militar Obrigatório!')
elif IdadeAtual > 18:
    TempoParaAlistar = IdadeAtual - 18
    print(f'Já passou a data do seu alistamento, você está atrasado {TempoParaAlistar} Anos!')
else:
    print('Você digitou algo errado, tente novamente.')