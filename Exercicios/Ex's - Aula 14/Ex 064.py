
contador_num = n = soma = 0
while n != 999:
        n = int(input('Digite um número inteiro: '))
        if n != 999:
            contador_num += 1
            soma += n
print(f'O total de número foi: {contador_num}')
print(f'A soma total do valores digitados foi: {soma}')