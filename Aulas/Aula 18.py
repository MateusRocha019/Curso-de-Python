'''
Aula 18 - Listas (Parte 2)

Listas compostas são listas que contêm outras listas como elementos. Elas permitem organizar dados de forma hierárquica e podem ser acessadas usando múltiplos índices. São como uma matriz, onde cada elemento da lista principal é uma linha e os elementos das listas internas são as colunas.

- Listas são estruturas de dados que permitem armazenar múltiplos valores em uma única variável. Elas são mutáveis, o que significa que podemos alterar seus elementos após a criação da lista.
- Podemos adicionar elementos a uma lista usando o método append() para adicionar no final ou insert()() para adicionar em uma posição específica. Para remover elementos, podemos usar del, pop() ou remove(). O método sort() organiza os elementos da lista em ordem crescente ou decrescente, e a função len() retorna o número de elementos na lista.
- O enumerate() permite iterar sobre os elementos da lista, retornando o índice e o valor de cada elemento. É importante entender a diferença entre atribuir uma lista a outra variável, que cria uma referência ao mesmo objeto, e criar uma cópia da lista usando fatiamento, que cria uma lista independente.

pessoas = [['Pedro', 25], ['Maria', 19], ['João', 32]]
print(pessoas[0][0]) -> Pedro
print(pessoas[1][1]) -> 19

- a primeira posição é a lista principal, e a segunda posição é o elemento dentro da lista interna.
 
teste = ['Ana', 25, 1.68]
galera = list()
galera.append(teste[:])
print(galera) -> [['Ana', 25, 1.68]]

teste[0, 1, 2] = 'Maria', 22, 1.55 ou teste = ['Maria', 22, 1.55]
galera.append(teste[:])
print(galera) -> [['Ana', 25, 1.68], ['Maria', 22, 1.55]]

galera.append(['João', 32, 1.75])
print(galera) -> [['Ana', 25, 1.68], ['Maria', 22, 1.55], ['João', 32, 1.75]]

- E para adicionar mais um posição na lista galera mas vazio a gente usa o append() com uma lista vazia, assim:
galera.append([])
print(galera) -> [['Ana', 25, 1.68], ['Maria', 22, 1.55], ['João', 32, 1.75], []]


- O método append() adiciona uma cópia da lista teste à lista galera, criando uma lista composta. O uso de teste[:] garante que uma cópia da lista teste seja adicionada, evitando que alterações na lista teste afetem a lista galera.

-Usando o for para percorrer a lista galera, podemos acessar cada elemento interno e imprimir seus valores de forma organizada. Por exemplo:
for p in galera:
    print(f'{p[0]} tem {p[1]} anos e mede {p[2]} metros.') 
    -> Ana tem 25 anos e mede 1.68 metros.
    -> Maria tem 22 anos e mede 1.55 metros.
    -> João tem 32 anos e mede 1.75 metros.

galera = list()
dado = list()
totalmaior = totalmenor = 0

for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()

print(galera) -> [['Ana', 25], ['Maria', 17], ['João', 32]]

for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totalmaior += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totalmenor += 1
print(f'Total de maiores de idade: {totalmaior}') 
print(f'Total de menores de idade: {totalmenor}')
    -> Ana é maior de idade.
    -> Maria é menor de idade.
    -> João é maior de idade.

'''