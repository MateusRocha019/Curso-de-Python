'''
Aula 20 - Funções (Parte 1)

Funções são blocos de código que realizam uma tarefa específica e podem ser reutilizados em diferentes partes de um programa. Elas ajudam a organizar o código, tornando-o mais legível e modular. Em Python, as funções são definidas usando a palavra-chave def, seguida pelo nome da função e parênteses que podem conter parâmetros.
- Funções podem receber argumentos, que são valores passados para a função quando ela é chamada, e podem retornar valores usando a palavra-chave return. Se uma função não tiver um return, ela retornará None por padrão.
- Funções podem ser definidas com parâmetros padrão, permitindo que sejam chamadas com menos argumentos do que o número de parâmetros definidos. Além disso, funções podem ter parâmetros nomeados, permitindo que os argumentos sejam passados em qualquer ordem. 

EXEMPLO 1:
def mensagem(msg):
    print('-' * 30)
    print(msg)
    print('-' * 30)

mensagem("Olá, mundo!")
    -> ------------------------------
    -> Olá, mundo!
    -> ------------------------------ 
mensagem("Bem-vindo ao curso de Python!")
    -> ------------------------------
    -> Bem-vindo ao curso de Python!
    -> ------------------------------

EXEMPLO 2:
def soma(a, b):
    s = a + b
    print(f'A soma de {a} + {b} é {s}')
soma(3, 5) -> A soma de 3 + 5 é 8
soma(8, 9) -> A soma de 8 + 9 é 17
soma(a=4, b=6) -> A soma de 4 + 6 é 10

EXEMPLO 3: Empacotamento de parâmetros
Empacotar parâmetros em uma função permite que você passe um número variável de argumentos para a função. Isso é feito usando o operador * antes do nome do parâmetro na definição da função. Dentro da função, os argumentos são acessíveis como uma tupla.

def contador(*num):
    print(f'Recebi {len(num)} números: {num}')
contador(2, 1, 7) -> Recebi 3 números: (2, 1, 7)
contador(8, 0) -> Recebi 2 números: (8, 0)

EXEMPLO 4: Desempacotamento de parâmetros
Desempacotar parâmetros em uma função permite que você passe os elementos de uma sequência como argumentos individuais para a função. Isso é feito usando o operador * antes do nome da variável que contém os valores.

def mostrar_valores(*valores):
    for v in valores:
        print(v)

mostrar_valores(2, 1, 7) 
                    -> 2
                    -> 1
                    -> 7

EXEMPLO 5: Função que dobra os valores de uma lista
def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1

valores = [7, 2, 5, 0, 4]
dobra(valores)
print(valores) -> [14, 4, 10, 0, 8]

#A Diferença entre passagem por valor e passagem por referência é que, na passagem por valor, a função recebe uma cópia do valor, enquanto na passagem por referência, a função recebe uma referência ao objeto original. Isso significa que alterações feitas no objeto dentro da função afetarão o objeto original fora da função.
#No exemplo acima, a função dobra() recebe uma lista como argumento. Como listas são objetos mutáveis em Python, a função modifica a lista original, dobrando cada elemento. Portanto, após a chamada da função, a lista valores é alterada.

EXEMPLO 6: Função com retorno de valores





'''