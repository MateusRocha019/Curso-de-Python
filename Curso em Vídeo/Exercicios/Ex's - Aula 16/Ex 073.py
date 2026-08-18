classificacao_brasileirao = (
    "Palmeiras",          # 1º - 48 pts
    "Flamengo",           # 2º - 45 pts
    "Athletico-PR",       # 3º - 41 pts
    "Fluminense",         # 4º - 38 pts
    "Cruzeiro",           # 5º - 36 pts
    "Bahia",              # 6º - 34 pts
    "Red Bull Bragantino",# 7º - 32 pts
    "Atlético-MG",        # 8º - 32 pts
    "Corinthians",        # 9º - 32 pts
    "Coritiba",           # 10º - 31 pts
    "Botafogo",           # 11º - 30 pts
    "Vitória",            # 12º - 29 pts
    "São Paulo",          # 13º - 27 pts
    "Santos",             # 14º - 25 pts
    "Grêmio",             # 15º - 25 pts
    "Mirassol",           # 16º - 23 pts
    "Internacional",      # 17º - 23 pts
    "Remo",               # 18º - 22 pts
    "Vasco da Gama",      # 19º - 22 pts
    "Chapecoense"         # 20º - 11 pts
)

print(f'Os primeiros 5 times da tabela são: {classificacao_brasileirao[0:6]}')
print(f'Os Últimos 4 colocados da tabela são: {classificacao_brasileirao[16:20]}')
print('Os times em ordem em alfabética são: ', sorted(classificacao_brasileirao))
print('A posição da Chapecoense é:', classificacao_brasileirao.index('Chapecoense') + 1)