print('====== Calculadora de média de notas ======')
nota1 = float(input('Digite o valor da primeira nota: '))
nota2 = float(input('Digite o valor da segunda nota: '))

media = round((nota1 + nota2) / 2, 2)
if media < 5:
    print(f'Sua média foi {media}, abaixo de 5.0 então está reprovado!')
elif media <= 6.99 and media >= 5.0:
    print(f'Sua média foi {media}, ficou entre 6.9 e 5.0, então está de recuperação!')
elif media >= 7.0:
    print(f'Parabéns você tirou de média {media}, acima de 7.0 e foi aprovado!')
else:
    print('Ocorreu algum erro, tente novamente!')
