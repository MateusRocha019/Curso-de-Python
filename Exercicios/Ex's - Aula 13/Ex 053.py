frase = input('Digite uma palavra ou frase para saber se é um palíndromo: ').replace(' ', '').lower()

frase_lista = list(frase)
tamanho_lista = len(frase_lista)

tras_para_frente = tamanho_lista - 1

for c in range(0,tamanho_lista):
    print(frase_lista[c])
    print(frase_lista[tras_para_frente])

    if frase_lista[c] != frase_lista[tras_para_frente]:
        print(f'A frase "{frase}" não um palíndromo!')
        break
    elif c == (tamanho_lista - 1):
        print(f'A frase "{frase}" é um palíndromo')
        break
    else:
        pass
    tras_para_frente = tras_para_frente - 1