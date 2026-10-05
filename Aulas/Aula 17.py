'''
Aula aprendendo sobre LISTAS.

lanches = ['Hamburguer', 'Suco', 'Pizza', 'Pudim']
-> ['Hamburguer', 'Suco', 'Pizza', 'Pudim']

lanches[3] = 'Picole' -> ['Hamburguer', 'Suco', 'Pizza', 'Picole']
- Atribuindo um novo valor a um índice específico da lista, substituindo o valor anterior.

lanches.append('Cookie') -> ['Hamburguer', 'Suco', 'Pizza', 'Picole', 'Cookie']
- append adiciona um elemento no final da lista.

lanches.insert(0, 'Cachorro Quente') -> ['Cachorro Quente', 'Hamburguer', 'Suco', 'Pizza', 'Picole', 'Cookie']
-  insert adiciona um elemento em uma posição específica da lista.

del lanches[3] ou lanches.pop(3) ou lanches.remove('Suco') -> ['Cachorro Quente', 'Hamburguer', 'Pizza', 'Picole', 'Cookie']
Ou seja, podemos remover um elemento da lista de três formas diferentes.

- o del remove o elemento pelo índice, mas não retorna o elemento removido.
- o pop remove o elemento pelo índice, mas retorna o elemento removido.
- o remove remove o elemento pelo valor, mas não retorna o elemento removido.
- o lanche.pop() remove o último elemento da lista, mas retorna o elemento removido.

ex: if 'Pizza' in lanches:
    lanches.remove('Pizza')
- Isso serve para verificar se um elemento está na lista antes de tentar removê-lo, evitando erros caso o elemento não exista.


valores = list(range(4, 11)) -> [4, 5, 6, 7, 8, 9, 10]
- A função range() gera uma sequência de números, e a função list() converte essa sequência em uma lista.

valores = [8, 2, 5, 4, 9, 3, 0]
valores.sort() -> [0, 2, 3, 4, 5, 8, 9]
- O método sort() organiza os elementos da lista em ordem crescente.

ou inverso 

valores.sort(reverse=True) -> [9, 8, 5, 4, 3, 2, 0]
- O parâmetro reverse=True organiza os elementos da lista em ordem decrescente.

len(lanches) -> 6
- A função len() retorna o número de elementos na lista.

valores = [8, 2, 5, 4, 9, 3, 0]
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
- O enumerate() retorna o índice e o valor de cada elemento da lista, permitindo iterar sobre eles de forma eficiente.


    Exemplo de ligação entre listas:
a = [2, 3, 4, 7]
b = a
b[2] = 8
- Isso demonstra que ao atribuir uma lista a outra variável, ambas apontam para o mesmo objeto na memória. Portanto, alterar um elemento em uma lista também altera o outro.
print(f'Lista A: {a}')
print(f'Lista B: {b}')
-> Lista A: [2, 3, 8, 7]

    Exemplo de cópia de listas:
a = [2, 3, 4, 7]
b = a[:]
b[2] = 8
- Isso demonstra que ao criar uma cópia de uma lista usando a notação de fatiamento (a[:]), as duas listas são independentes. Alterar um elemento em uma lista não afeta a outra.
print(f'Lista A: {a}')  -> Lista A: [2, 3, 4, 7]
print(f'Lista B: {b}')  -> Lista B: [2, 3, 8, 7]   


'''