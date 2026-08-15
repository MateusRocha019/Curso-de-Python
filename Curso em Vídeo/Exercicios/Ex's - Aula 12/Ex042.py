print('====== Condição de Existência de um Triângulo ======\n')

a = float(input('Digite o valor da primeira reta: '))
b = float(input('Digite o valor da segunda reta: '))
c = float(input('Digite o valor da terceira reta: \n'))

def identificar_triangulo():
    if a == b == c:
        print('Como todas as retas são iguais o triangulo a montar é Equilátero')
    elif a != b and b != c and c != a:
        print('Como todas as retas são diferentes você monta um triangulo Escaleno')
    else:
        print('Como 2 retas são iguais você montra um triangulo Isósceles')



if a > b and a > c:
    teste = b + c
    if teste > a:
        print('Você consegue montar um triangulo')
        identificar_triangulo()
    else:
        print('Você não consegue montar um triangulo')
elif b > a and b > c:
    teste = a + c
    if teste > b:
        print('Você consegue montar um triangulo')
        identificar_triangulo()
    else:
        print('Você não consegue montar um triangulo')
else:
    teste = a + b
    if teste > c:
        print('Você consegue montar um triangulo')
        identificar_triangulo()
    else:
        print('Você não consegue montar um triangulo')


