ValorCasa = float(input('Qual o valor da casa? '))
Salario = float(input('Qual é o seu salário? '))
TempoPagarAnos = int(input('Em quanto anos deseja pagar? '))

TempoPagarMeses = TempoPagarAnos * 12
ValorMensalMinino = ValorCasa / TempoPagarMeses
ValorMensal = (Salario * 30) / 100


if ValorMensal >= ValorMensalMinino:
    print(f"O Valor mensal a pagar será: {ValorMensalMinino}")
else:
    print('Infelizmente a parcela ficou maior que os 30% do seu salário.')