'''
Aula 21 

Interactive Help
O Python possui uma função interna chamada help() que fornece informações sobre funções, módulos e objetos.

Docstrings
Docstrings são strings de documentação que descrevem o propósito e o comportamento de funções, classes e módulos. Elas são definidas usando aspas triplas (''' ''' ou """ """) logo após a definição da função, classe ou módulo.
As docstrings podem ser acessadas usando a função help() ou o atributo __doc__ do objeto.
Exemplo de docstring em uma função:

contador(inicio, fim, passo)
    """
    Função que realiza uma contagem de números.
    
    Parâmetros:
    inicio (int): O número inicial da contagem.
    fim (int): O número final da contagem.
    passo (int): O incremento ou decremento entre os números da contagem.
    
    Retorna:
    None
    """
    # Corpo da função
como usar a função help() para acessar a docstring:
help(contador)


Argumentos Opcionais
Em Python, funções podem ter argumentos opcionais, que são parâmetros com valores padrão. Se o chamador da função não fornecer um valor para esses parâmetros, os valores padrão serão usados.
Exemplo de função com argumentos opcionais:
def soma(a, b=0):
    """
    Função que realiza a soma de dois números.
    
    Parâmetros:
    a (int): O primeiro número.
    b (int, opcional): O segundo número. Valor padrão é 0.
    
    Retorna:
    int: A soma de a e b.
    """
    return a + b
print(soma(5))  # Saída: 5
print(soma(5, 3))  # Saída: 8

Escopo de Variáveis
O escopo de uma variável determina onde ela pode ser acessada dentro do código. Em Python, existem dois tipos principais de escopo: local e global. Variáveis definidas dentro de uma função têm escopo local, enquanto variáveis definidas fora de qualquer função têm escopo global.

def teste(b):
    a = 8  # Variável local
    b += 4
    c = 2  # Variável local
    print(f"A dentro vale {a}")
    print(f"B dentro vale {b}")
    print(f"C dentro vale {c}")

a = 5  # Variável global
teste(a)
print(f"A fora vale {a}")  # A variável global 'a' não é afetada pela função teste

def teste(b):
    global a  # Declara que 'a' é uma variável global
    a = 8  # Modifica a variável global 'a'
    b += 4
    c = 2  # Variável local
    print(f"A dentro vale {a}")
    print(f"B dentro vale {b}")
    print(f"C dentro vale {c}")
a = 5  # Variável global
teste(a)
print(f"A fora vale {a}")  # A variável global 'a' foi modificada

Agora usando o RETURN

Ex:
def somar(a=0, b=0, c=0):
    """
    Função que realiza a soma de até três números.
    
    Parâmetros:
    a (int, opcional): O primeiro número. Valor padrão é 0.
    b (int, opcional): O segundo número. Valor padrão é 0.
    c (int, opcional): O terceiro número. Valor padrão é 0.
    
    Retorna:
    int: A soma de a, b e c.
    """
    s = a + b + c
    return s

soma1 = somar(3, 2, 5)
soma2 = somar(2, 2)
print(f"As somas foram {soma1} e {soma2}")

'''