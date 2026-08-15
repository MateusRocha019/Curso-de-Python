num = 1
media = 0
contador = 0
verificador = 'S'
maior = menor = somador = 0

while verificador == 'S':
    while num != 0:
        num = int(input('Digite um número: '))
        print('Se desejar parar digite: 0\n')
        somador += num
        contador += 1
        if contador == 1:
            menor = num
            maior = num
        if num > maior:
            maior = num
        if num < menor and num != 0:
            menor = num
    contador = contador - 1
    media = somador / contador
    print(f'A média entre todos os números digitados é: {media:.2f}')
    print(f'O maior valor digitado é: {maior}')
    print(f'O menor valor digitado é: {menor}\n')

    verificador = input('Quer continuar a digitar valores? (S/N): \n').upper()
    num = 1
