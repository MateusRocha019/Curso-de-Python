n = int(input('Digite um número para saber a sequencia de fibonacci: '))
cont = 0
anterior1 = 0
anterior2 = 1
resultado = 0
while cont != n:

    if cont < 2:
        print(cont, end=' ')

    else:
        resultado = anterior1 + anterior2
        print(resultado, end=' ')
        anterior1 = anterior2
        anterior2 = resultado
    cont += 1