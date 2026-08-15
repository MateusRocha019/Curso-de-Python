from datetime import date
ano = date.today().year

maiores = 0
menores = 0

for c in range(1,8):
    aniversario = int(input(f"Digite a data de aniversário da {c}º pessoa:"))
    if aniversario > ano:
        print('Você digitou um ano maior que o atual! Tente novamente.')
        break
    idade = ano - aniversario
    if idade >= 18:
        maiores = maiores + 1
    elif idade < 18:
        menores = menores + 1

    if c == 7:

        print(f'\n{maiores} Pessoas são maiores de idade!')
        print(f'{menores} Pessoas são menores de idade!')


