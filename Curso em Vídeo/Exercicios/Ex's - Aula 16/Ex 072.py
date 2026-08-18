numeros_extenso = (
    "zero", "um", "dois", "três", "quatro",
    "cinco", "seis", "sete", "oito", "nove",
    "dez", "onze", "doze", "treze", "quatorze",
    "quinze", "dezesseis", "dezessete", "dezoito", "dezenove",
    "vinte")
while True:
    num = int(input('Digite um número de 0 a 20: '))
    if num >= 0 and num <= 20:
        print(f'Você digitou o número {numeros_extenso[num]}')
        break
    else:
        print('Você digitou algo errado tente novamente!')
