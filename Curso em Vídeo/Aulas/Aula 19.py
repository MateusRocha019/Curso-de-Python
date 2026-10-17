"""
Aula 19 - Dicionários em Python

dados = dict() ou dados = {}  # Cria um dicionário vazio
dados = {'nome': 'Pedro', 'idade': 25}  # Cria um dicionário com dados
print(dados['nome'])  # Acessa o valor associado à chave 'nome'
print(dados['idade'])  # Acessa o valor associado à chave 'idade'

dados['sexo'] = 'M'  # Adiciona um novo par chave-valor ao dicionário
print(dados) -> {'nome': 'Pedro', 'idade': 25, 'sexo': 'M'}

del dados['idade']  # Remove o par chave-valor associado à chave 'idade'
print(dados) -> {'nome': 'Pedro', 'sexo': 'M'}

filmes = {'nome': 'Star Wars',
          'ano': 1977,
          'diretor': 'George Lucas'
          }
print(filmes.values())  # Retorna os valores do dicionário -> dict_values(['Star Wars', 1977, 'George Lucas'])
print(filmes.keys())  # Retorna as chaves do dicionário -> dict_keys(['nome', 'ano', 'diretor'])
print(filmes.items())  # Retorna os pares chave-valor do dicionário -> dict_items([('nome', 'Star Wars'), ('ano', 1977), ('diretor', 'George Lucas')])

for k, v in filmes.items():  # Itera sobre os pares chave-valor do dicionário
    print(f'O {k} é {v}')  # Imprime cada chave e valor
    -> O nome é Star Wars
    -> O ano é 1977
    -> O diretor é George Lucas

locadora = []
locadora.append(filmes)  # Adiciona o dicionário 'filmes
' à lista 'locadora' -> [{'nome': 'Star Wars', 'ano': 1977, 'diretor': 'George Lucas'}]
print(locadora)  # Imprime a lista 'locadora' -> [{'nome': 'Star Wars', 'ano': 1977, 'diretor': 'George Lucas'}]
filmes2 = {'nome': 'Avengers',
           'ano': 2012,
           'diretor': 'Joss Whedon'
           }
locadora.append(filmes2)  # Adiciona o dicionário 'filmes2' à lista 'locadora'
print(locadora)  # Imprime a lista 'locadora' -> [{'nome': 'Star Wars', 'ano': 1977, 'diretor': 'George Lucas'}, {'nome': 'Avengers', 'ano': 2012, 'diretor': 'Joss Whedon'}]
print(locadora[0]['nome'])  # Acessa o valor associado à chave 'nome' do primeiro dicionário na lista 'locadora' -> Star Wars
print(locadora[1]['nome'])  # Acessa o valor associado à chave 'nome' do segundo dicionário na lista 'locadora' -> Avengers

print(locadora[0])  # Imprime o primeiro dicionário na lista 'locadora' -> {'nome': 'Star Wars', 'ano': 1977, 'diretor': 'George Lucas'}
print(locadora[1])  # Imprime o segundo dicionário na lista 'locadora' -> {'nome': 'Avengers', 'ano': 2012, 'diretor': 'Joss Whedon'}

estado = dict()
brasil = list()

for c in range(0, 3):
    estado['uf'] = input('Unidade Federativa: ')
    estado['sigla'] = input('Sigla do Estado: ')
    brasil.append(estado.copy())  # Adiciona uma cópia do dicionário 'estado' à lista 'brasil'
print(brasil)  # Imprime a lista 'brasil' -> [{'uf': 'Minas Gerais', 'sigla': 'MG'}, {'uf': 'São Paulo', 'sigla': 'SP'}, {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}]
for e in brasil:
    for k, v in e.items():  # Itera sobre os pares chave-valor do dicionário 'e'
        print(f'O campo {k} tem valor {v}')  # Imprime cada chave e valor
        -> O campo uf tem valor Minas Gerais
        -> O campo sigla tem valor MG
        -> O campo uf tem valor São Paulo
        -> O campo sigla tem valor SP
        -> O campo uf tem valor Rio de Janeiro
        -> O campo sigla tem valor RJ
    
 


"""