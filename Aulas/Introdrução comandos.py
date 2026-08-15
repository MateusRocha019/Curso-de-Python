# =====================================================================
# GUIA PRÁTICO: FUNDAMENTOS DO PYTHON
# Copie, cole na sua IDE e execute para ver a mágica acontecer!
# =====================================================================

# ---------------------------------------------------------------------
# 1. VARIÁVEIS E TIPOS DE DADOS
# ---------------------------------------------------------------------
print("--- 1. Variáveis e Tipos de Dados ---")

nome = "Dev Pythonico"       # String (texto, sempre entre aspas)
idade = 25                  # Integer (número inteiro)
altura = 1.75               # Float (número decimal, usa ponto)
esta_estudando = True       # Boolean (True ou False - sempre maiúsculo)

# Usamos f-strings (f"...") para misturar texto e variáveis facilmente usando {}
print(f"Nome: {nome} | Tipo: {type(nome)}")
print(f"Idade: {idade} anos | Tipo: {type(idade)}")
print(f"Altura: {altura}m | Tipo: {type(altura)}")
print(f"Estudando? {esta_estudando} | Tipo: {type(esta_estudando)}\n")


# ---------------------------------------------------------------------
# 2. OPERADORES MATEMÁTICOS
# ---------------------------------------------------------------------
print("--- 2. Operadores Matemáticos ---")

soma = 10 + 5
subtracao = 10 - 5
multiplicacao = 10 * 5
divisao = 10 / 3           # Divisão comum (retorna float)
divisao_inteira = 10 // 3  # Descarta as casas decimais
resto = 10 % 3             # Resto da divisão (operador módulo)
potencia = 2 ** 3          # Exponenciação (2 elevado a 3)

print(f"10 + 5 = {soma}")
print(f"10 / 3 = {divisao:.2f}")  # ':.2f' limita para 2 casas decimais
print(f"Divisão inteira de 10 por 3 = {divisao_inteira}")
print(f"Resto da divisão de 10 por 3 = {resto}")
print(f"2 elevado a 3 = {potencia}\n")


# ---------------------------------------------------------------------
# 3. ESTRUTURAS CONDICIONAIS (Tomada de Decisão)
# ---------------------------------------------------------------------
print("--- 3. Estruturas Condicionais (if/elif/else) ---")

# ATENÇÃO: Repare no recuo (indentação) de 4 espaços antes dos prints.
# No Python, é o espaçamento que define o que está dentro da condição!
idade_usuario = 18

if idade_usuario >= 18:
    print("Resultado: Você é maior de idade. Acesso liberado!")
elif idade_usuario == 17:
    print("Resultado: Quase lá! Volte quando fizer 18 anos.")
else:
    print("Resultado: Menor de idade. Acesso bloqueado.")
print() # Apenas pula uma linha no terminal


# ---------------------------------------------------------------------
# 4. COLEÇÕES (Listas e Dicionários)
# ---------------------------------------------------------------------
print("--- 4. Coleções de Dados ---")

# LISTAS: Coleções ordenadas. A contagem dos elementos começa no índice 0!
tecnologias = ["Python", "JavaScript", "SQL"]
print(f"Lista original: {tecnologias}")
print(f"Primeiro elemento (índice 0): {tecnologias[0]}")

tecnologias.append("Docker") # .append() adiciona um item ao final da lista
print(f"Lista atualizada: {tecnologias}\n")

# DICIONÁRIOS: Guardam informações no formato Chave : Valor
usuario = {
    "nome": "Amanda",
    "cargo": "Desenvolvedora",
    "experiencia_anos": 3
}
print(f"Dicionário completo: {usuario}")
print(f"Acessando apenas o cargo: {usuario['cargo']}\n")


# ---------------------------------------------------------------------
# 5. ESTRUTURAS DE REPETIÇÃO (Loops/Laços)
# ---------------------------------------------------------------------
print("--- 5. Estruturas de Repetição (for/while) ---")

# LOOP FOR: Ideal para percorrer listas ou repetir algo um número fixo de vezes
print("Percorrendo a lista com FOR:")
for tech in tecnologias:
    print(f" -> Aprendendo: {tech}")

print("\nUsando range(3) no FOR (repete de 0 a 2):")
for numero in range(3):
    print(f" -> Passo {numero}")

# LOOP WHILE: Executa enquanto uma condição for Verdadeira
print("\nContagem com WHILE:")
energia = 3
while energia > 0:
    print(f" -> Bateria em {energia}0%...")
    energia -= 1 # Reduz 1 a cada volta para evitar um loop infinito!
print("Bateria zerada!\n")


# ---------------------------------------------------------------------
# 6. FUNÇÕES (Blocos de Código Reutilizáveis)
# ---------------------------------------------------------------------
print("--- 6. Funções ---")

# Criamos uma função usando 'def'. Ela recebe parâmetros e pode retornar dados.
def calcular_media(nota1, nota2):
    media = (nota1 + nota2) / 2
    return media # Devolve o valor calculado para quem chamou a função

# Chamando a função

# =====================================================================
# GUIA PRÁTICO: FUNDAMENTOS DO PYTHON (PARTE 2)
# Os conceitos que transformam você em um programador completo!
# =====================================================================

# ---------------------------------------------------------------------
# 7. OUTRAS COLEÇÕES: TUPLAS E SETS (CONJUNTOS)
# ---------------------------------------------------------------------
print("--- 7. Tuplas e Sets ---")

# TUPLA (usa parênteses): É idêntica à lista, mas IMUTÁVEL.
# Uma vez criada, você não pode alterar, adicionar ou remover itens. Segurança de dados!
coordenadas = (40.7128, -74.0060)
print(f"Tupla (Imutável): {coordenadas}")

# SET (usa chaves, mas sem chave:valor): Coleção que NÃO aceita itens duplicados.
# Muito útil para limpar dados repetidos.
usuarios_id = {101, 102, 103, 101, 102} # Note os IDs repetidos
print(f"Set (Apenas valores únicos): {usuarios_id}\n")


# ---------------------------------------------------------------------
# 8. TRATAMENTO DE ERROS (try / except)
# ---------------------------------------------------------------------
print("--- 8. Tratamento de Erros (Prevenindo Crash) ---")

# Na vida real, erros acontecem (divisão por zero, arquivo que não existe).
# Com try/except, seu programa não "morre" quando dá erro.
try:
    numero = int("não é um número") # Isso vai gerar um erro de conversão (ValueError)
    resultado = 10 / 0
except ValueError:
    print("Erro tratado: Você tentou converter um texto inválido em número!")
except ZeroDivisionError:
    print("Erro tratado: Não é possível dividir por zero!")
finally:
    print("O bloco 'finally' sempre roda, independente de ter dado erro ou não.\n")


# ---------------------------------------------------------------------
# 9. MANIPULAÇÃO DE ARQUIVOS (Escrever e Ler arquivos)
# ---------------------------------------------------------------------
print("--- 9. Criando e Lendo Arquivos ---")

# O 'with' garante que o arquivo seja fechado automaticamente após o uso
# 'w' = write (escrever/criar) | 'r' = read (ler)
with open("meu_arquivo.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write("Este é um arquivo criado automaticamente pelo Python!\n")
    arquivo.write("Segunda linha do arquivo.")

print("Arquivo 'meu_arquivo.txt' criado com sucesso!")

# Lendo o arquivo que acabamos de criar
with open("meu_arquivo.txt", "r", encoding="utf-8") as arquivo:
    conteudo = arquivo.read()
    print("Conteúdo lido do arquivo:")
    print(f"[{conteudo}]\n")


# ---------------------------------------------------------------------
# 10. IMPORTANDO MÓDULOS (Bibliotecas nativas)
# ---------------------------------------------------------------------
print("--- 10. Importando Módulos ---")

# O Python vem com muitas ferramentas prontas (bateria inclusa). Só precisamos importar.
import math
import random

numero_aleatorio = random.randint(1, 100) # Gera número de 1 a 100
raiz_quadrada = math.sqrt(25)

print(f"Número aleatório gerado: {numero_aleatorio}")
print(f"Raiz quadrada de 25: {raiz_quadrada}\n")


# ---------------------------------------------------------------------
# 11. LIST COMPREHENSION (A Mágica do Python)
# ---------------------------------------------------------------------
print("--- 11. List Comprehensions (Atalhos elegantes) ---")

# Criar uma nova lista a partir de outra de um jeito super rápido e legível.
precos_antigos = [10, 20, 30, 40]

# Forma tradicional com 3 linhas:
# precos_novos = []
# for preco in precos_antigos:
#     precos_novos.append(preco * 2)

# Forma Pythonica (List Comprehension) em 1 linha:
precos_novos = [preco * 2 for preco in precos_antigos]
print(f"Preços originais: {precos_antigos}")
print(f"Preços dobrados com list comp: {precos_novos}\n")


# ---------------------------------------------------------------------
# 12. INTRODUÇÃO À ORIENTAÇÃO A OBJETOS (Classes e Objetos)
# ---------------------------------------------------------------------
print("--- 12. Programação Orientada a Objetos (Classes) ---")

# Classes são "moldes" para criar objetos do mundo real com características (atributos) e ações (métodos)
class Cachorro:
    # O construtor define o que todo cachorro precisa ter ao "nascer"
    def __init__(self, nome, raca):
        self.nome = nome
        self.raca = raca

    # Um método (função dentro da classe) representando uma ação
    def latir(self):
        return f"{self.nome} diz: Au au!"

# Criando "objetos" (instâncias) a partir do molde
dog1 = Cachorro("Rex", "Pastor Alemão")
dog2 = Cachorro("Mel", "Poodle")

print(f"Meu cachorro: {dog1.nome} (Raça: {dog1.raca})")
print(dog1.latir())
print(dog2.latir())

print("\n=====================================================================")
print("Agora sim! Com a Parte 1 e Parte 2, você tem a base completa do Python.")
print("=====================================================================")

# =====================================================================
# GUIA PRÁTICO: FUNDAMENTOS DO PYTHON (PARTE 3 - O GRANDE FINAL)
# Recursos avançados e padrões que você verá em códigos profissionais!
# =====================================================================

# ---------------------------------------------------------------------
# 13. PARÂMETROS DINÂMICOS (*args e **kwargs)
# ---------------------------------------------------------------------
print("--- 13. Parâmetros Dinâmicos (*args e **kwargs) ---")

# Às vezes você não sabe quantos argumentos sua função vai receber.
# *args: Recebe múltiplos argumentos como uma TUPLA.
# **kwargs: Recebe múltiplos argumentos nomeados como um DICIONÁRIO.

def super_funcao(*args, **kwargs):
    print(f"Argumentos posicionais (args): {args}")
    print(f"Argumentos nomeados (kwargs): {kwargs}")

# Testando a função com qualquer quantidade de dados
super_funcao("Python", 2026, True, usuario="Amanda", nivel="Senior")
print()


# ---------------------------------------------------------------------
# 14. MÉTODOS MÁGICOS / DUNDER METHODS (__str__, __len__)
# ---------------------------------------------------------------------
print("--- 14. Métodos Mágicos (Dunder Methods) ---")

# São métodos com duplo underline (double underscore = dunder).
# Eles dizem ao Python como o seu objeto deve se comportar com funções nativas (como print() ou len()).

class Livro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    # Define o que aparece quando damos 'print()' no objeto
    def __str__(self):
        return f"'{self.titulo}' por {self.autor}"

    # Define o que o comando 'len()' retorna para este objeto
    def __len__(self):
        return self.paginas

meu_livro = Livro("Pense em Python", "Allen B. Downey", 240)

print(meu_livro)        # Usa o __str__ por trás dos panos
print(f"Páginas: {len(meu_livro)}")  # Usa o __len__ por trás dos panos
print()


# ---------------------------------------------------------------------
# 15. FUNÇÕES LAMBDA, MAP E FILTER
# ---------------------------------------------------------------------
print("--- 15. Lambda, Map e Filter (Programação Funcional) ---")

# Lambdas são funções anônimas de uma única linha.
dobrar = lambda x: x * 2
print(f"Dobro de 5 usando Lambda: {dobrar(5)}")

# Usando lambdas com 'map' (aplica uma função a todos os itens de uma lista)
numeros = [1, 2, 3, 4]
dobrados = list(map(lambda x: x * 2, numeros))
print(f"Lista dobrada com Map: {dobrados}")

# Usando lambdas com 'filter' (filtra itens que atendem a uma condição)
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(f"Apenas os pares com Filter: {pares}\n")


# ---------------------------------------------------------------------
# 16. GENERATORS E YIELD (Economia extrema de memória)
# ---------------------------------------------------------------------
print("--- 16. Generators e 'yield' ---")

# Se você precisa processar uma lista de 1 milhão de itens, criar uma lista na memória vai travar seu PC.
# O 'yield' cria um gerador que entrega UM item por vez, sob demanda, sem gastar memória.

def gerador_de_numeros():
    yield 1
    yield 2
    yield 3

meu_gerador = gerador_de_numeros()
print(next(meu_gerador))  # Entrega o primeiro
print(next(meu_gerador))  # Entrega o segundo
print(next(meu_gerador))  # Entrega o terceiro
# print(next(meu_gerador)) # Se chamar de novo, dá erro porque acabou!
print()


# ---------------------------------------------------------------------
# 17. DECORADORES (Decorators - @)
# ---------------------------------------------------------------------
print("--- 17. Decoradores (Decorators) ---")

# Um decorador é uma função que envolve outra função para modificar ou monitorar o comportamento dela.
# É muito usado para medir tempo de execução, verificar se o usuário está logado, etc.

def meu_decorador(funcao_original):
    def wrapper():
        print("[Log] Executando algo ANTES da função principal...")
        funcao_original()
        print("[Log] Executando algo DEPOIS da função principal...")
    return wrapper

@meu_decorador  # Aplicando o decorador
def minha_funcao():
    print("   --> Olá! Eu sou a função principal!")

minha_funcao()

print("\n=====================================================================")
print("FIM DA TRILHA DE FUNDAMENTOS! Você tem 100% da base do Python aqui.")
print("=====================================================================")

# =====================================================================
# GUIA PRÁTICO: FUNDAMENTOS DO PYTHON (PARTE 4 - RECURSOS MODERNOS)
# Os toques finais para dominar o Python moderno de ponta a ponta!
# =====================================================================

# ---------------------------------------------------------------------
# 18. PATTERN MATCHING (O "Switch/Case" do Python)
# ---------------------------------------------------------------------
print("--- 18. Pattern Matching (match/case) ---")

# Introduzido no Python moderno, substitui sequências longas de if/elif.
# O caractere '_' funciona como o "case default" (se nenhuma opção bater).

comando = "iniciar"

match comando:
    case "iniciar" | "start":  # O caractere '|' funciona como "OU"
        print("-> Sistema iniciando...")
    case "parar":
        print("-> Sistema parando...")
    case _:
        print("-> Comando não reconhecido!")
print()


# ---------------------------------------------------------------------
# 19. TYPE HINTING (Anotações de Tipo)
# ---------------------------------------------------------------------
print("--- 19. Type Hinting (Anotações de Tipo) ---")

# Python é dinâmico, mas em projetos profissionais usamos "Dicas de Tipo"
# para ajudar a IDE a nos dar autocompletar e evitar erros de lógica.
# ': int' diz o tipo esperado do argumento, e '-> str' diz o tipo do retorno.

def repetir_palavra(palavra: str, vezes: int) -> str:
    return palavra * vezes

resultado_tipo = repetir_palavra("Python! ", 3)
print(f"Resultado tipado: {resultado_tipo}\n")


# ---------------------------------------------------------------------
# 20. OPERADOR WALRUS (Atribuição em Expressões - :=)
# ---------------------------------------------------------------------
print("--- 20. Operador Walrus (:=) ---")

# O operador ':=' permite que você crie e atribua um valor a uma variável
# diretamente dentro de uma expressão (como em um 'if' ou 'while').

texto = "Python_e_fantastico"

# Aqui nós medimos o tamanho, guardamos na variável 'n' e já fazemos o teste do 'if', tudo na mesma linha!
if (n := len(texto)) > 10:
    print(f"O texto é muito longo! Ele tem {n} caracteres.")
print()


# ---------------------------------------------------------------------
# 21. EXPRESSÕES CONDICIONAIS (Operador Ternário)
# ---------------------------------------------------------------------
print("--- 21. Operador Ternário ---")

# Uma forma elegante de escrever um 'if/else' simples em apenas uma linha.
idade = 20

# [Valor se verdadeiro] if [Condição] else [Valor se falso]
status = "Maior de idade" if idade >= 18 else "Menor de idade"
print(f"Status do usuário: {status}\n")


# ---------------------------------------------------------------------
# 22. ESCOPO DE VARIÁVEIS (global e nonlocal)
# ---------------------------------------------------------------------
print("--- 22. Escopo de Variáveis (global) ---")

# Variáveis criadas fora de funções são globais.
# Se você quiser alterar uma variável global dentro de uma função, precisa avisar o Python.

contador_global = 10

def alterar_global():
    global contador_global # Sem essa linha, o Python criaria uma variável local nova
    contador_global = 20

print(f"Antes da função: {contador_global}")
alterar_global()
print(f"Depois da função: {contador_global}\n")


# ---------------------------------------------------------------------
# 23. MÉTODOS ESSENCIAIS DE STRINGS (Manipulação de Texto)
# ---------------------------------------------------------------------
print("--- 23. Métodos Essenciais de Strings ---")

# Como programamos muito manipulando textos, estes métodos salvam vidas:
dados_sujos = "   pYtHoN, jAvAsCrIpT, sQl   "

# 1. split(): Corta o texto baseado em um caractere e transforma em lista
lista_dados = dados_sujos.split(",")

# 2. strip() e lower(): Remove espaços inúteis e padroniza para minúsculo usando List Comp
dados_limpos = [item.strip().lower() for item in lista_dados]

# 3. join(): Junta os elementos de uma lista usando um separador
texto_formatado = " | ".join(dados_limpos)

print(f"Original: '{dados_sujos}'")
print(f"Formatado: '{texto_formatado}'")

print("\n=====================================================================")
print("PRONTO! Sua enciclopédia pessoal de fundamentos do Python está completa.")
print("=====================================================================")

# =====================================================================
# GUIA PRÁTICO: FUNDAMENTOS DO PYTHON (PARTE 5 - AJUSTE FINO)
# Comportamentos de memória, truques de depuração e estrutura de scripts!
# =====================================================================

import copy


# ---------------------------------------------------------------------
# 24. ESTRUTURA DE SCRIPT SEGURO (if __name__ == "__main__")
# ---------------------------------------------------------------------
# Quando você importa um arquivo Python em outro, ele executa todo o código dele.
# Para evitar que códigos de teste rodem ao importar, usamos este bloco.
# Ele garante que o código abaixo só rode se você executar ESTE arquivo diretamente.

def funcao_principal():
    print("--- 24. Estrutura de Script Seguro ---")
    print("-> Este script foi executado diretamente pelo usuário!\n")


# ---------------------------------------------------------------------
# 25. ENUMERATE E ZIP (Utilitários de Loops)
# ---------------------------------------------------------------------
def utilitarios_de_loop():
    print("--- 25. Enumerate e Zip ---")

    nomes = ["Alice", "Bob", "Charlie"]
    pontos = [85, 90, 95]

    # enumerate(): Dá acesso ao índice e ao valor ao mesmo tempo
    print("Usando enumerate():")
    for indice, nome in enumerate(nomes):
        print(f" -> Posição {indice}: {nome}")

    # zip(): Junta duas ou mais listas para iterar em paralelo
    print("\nUsando zip() para juntar listas:")
    for nome, pontuacao in zip(nomes, pontos):
        print(f" -> {nome} fez {pontuacao} pontos.")
    print()


# ---------------------------------------------------------------------
# 26. IDENTIDADE VS IGUALDADE (is vs ==) E TRUTHY/FALSY
# ---------------------------------------------------------------------
def identidade_e_valores():
    print("--- 26. Identidade (is) vs Igualdade (==) ---")

    # '==' compara os VALORES. 'is' compara se são o MESMO objeto na memória.
    lista_a = [1, 2, 3]
    lista_b = [1, 2, 3]
    lista_c = lista_a

    print(f"lista_a == lista_b? {lista_a == lista_b}")  # True (valores iguais)
    print(f"lista_a is lista_b? {lista_a is lista_b}")  # False (espaços diferentes na memória)
    print(f"lista_a is lista_c? {lista_a is lista_c}")  # True (apontam para a mesma lista)

    # TRUTHY E FALSY: No Python, objetos vazios ([], {}, ""), o número 0 e None
    # são considerados "False" em estruturas condicionais sem precisar de comparação.
    lista_vazia = []
    if not lista_vazia:
        print("-> Listas vazias são tratadas como Falsy no Python.")
    print()


# ---------------------------------------------------------------------
# 27. REFERÊNCIA VS CÓPIA (Shallow vs Deep Copy)
# ---------------------------------------------------------------------
def demonstracao_copias():
    print("--- 27. Cópia Rasa vs Cópia Profunda ---")

    # Se você copiar uma lista usando '=', você copia apenas a REFERÊNCIA.
    # Alterar a cópia vai alterar a original!
    original = [[1, 2], [3, 4]]

    # Cópia Rasa (Shallow Copy): Copia a estrutura, mas sublistas ainda compartilham memória
    copia_rasa = list(original)

    # Cópia Profunda (Deep Copy): Copia tudo de forma 100% independente
    copia_profunda = copy.deepcopy(original)

    # Alterando a sublista da original
    original[0][0] = 99

    print(f"Original modificada: {original}")
    print(f"Cópia Rasa (também mudou): {copia_rasa}")
    print(f"Cópia Profunda (protegida): {copia_profunda}\n")


# ---------------------------------------------------------------------
# 28. F-STRING PARA DEBUTAÇÃO (Truque de Produtividade)
# ---------------------------------------------------------------------
def fstring_avancado():
    print("--- 28. Depuração Rápida com f-strings ---")

    usuario = "Carlos"
    projeto_ativo = True

    # Adicionar um sinal de '=' dentro das chaves da f-string imprime o nome da variável e o valor.
    # Perfeito para prints rápidos de debug sem precisar escrever texto explicativo.
    print(f"{usuario=}")
    print(f"{projeto_ativo=}\n")


# ---------------------------------------------------------------------
# 29. GERENCIADOR DE CONTEXTO PERSONALIZADO (with customizado)
# ---------------------------------------------------------------------
# Como criar o seu próprio bloco "with" usando os métodos mágicos de contexto.

class ConexaoBancoDados:
    def __enter__(self):
        print(" -> [Setup] Conectando ao Banco de Dados...")
        return self  # Retorna o objeto para ser usado dentro do bloco 'with'

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(" -> [Teardown] Fechando conexões e limpando memória.")
        # Se ocorrer um erro dentro do bloco 'with', ele passa por aqui antes do programa fechar.


def testar_contexto():
    print("--- 29. Gerenciador de Contexto Customizado ---")
    with ConexaoBancoDados() as conexao:
        print("    [Execução] Executando query SQL...")
    print()


# Executando todas as funções de forma organizada
if __name__ == "__main__":
    funcao_principal()
    utilitarios_de_loop()
    identidade_e_valores()
    demonstracao_copias()
    fstring_avancado()
    testar_contexto()

    print("=====================================================================")
    print("PARABÉNS! Você esgotou todos os fundamentos possíveis do Python.")
    print("=====================================================================")