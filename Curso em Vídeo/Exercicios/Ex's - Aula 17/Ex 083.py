frase = list(input('Digite a expressão matématica usando parentêses: '))
teste = 0
print(frase)
print(len(frase))

parenteseAberto = parenteseFechado = 0

for c in range(0,len(frase)):
    if frase[c] in '()':
        if frase[c] == '(':
            parenteseAberto += 1
        else:
            parenteseFechado += 1
    if parenteseAberto < parenteseFechado:
        teste = 1
        break
if teste != 1 and parenteseAberto == parenteseFechado:
    print('Sua expressão está correta!')
if teste == 1 or parenteseAberto != parenteseFechado:
    print("Sua Expressão está errada!")