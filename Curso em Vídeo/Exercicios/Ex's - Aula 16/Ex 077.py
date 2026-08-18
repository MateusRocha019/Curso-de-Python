palavras = ('aprender', 'codigo', 'python', 'teclado', 'desafio', 'futuro', 'sucesso', 'pratica', 'logica', 'projeto')
for palavra in palavras:
    print()
    print(f'Na palavraa {palavra.upper().} temos ', end='')
    for c in palavra.upper():
        if c in 'AEIOU':
            print(c, end=' ')