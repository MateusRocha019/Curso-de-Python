#Laços de Repetição
soma = quant = 0
print('Soma dos números\nPara finalizar digite 999\n')
while True:
    num =  int(input('Digite um número: '))
    if num == 999:
        break
    soma += num
    quant += 1
print(f'O total de números digitados foi {quant} e a soma deles deu858 {soma}!')
