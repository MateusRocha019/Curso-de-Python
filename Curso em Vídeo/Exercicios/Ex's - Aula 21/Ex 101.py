import datetime

data = ano = 0
def voto(ano):
    global data
    data = datetime.date.today().year - ano
    if data < 16:
        return "NEGADO"
    elif 18 > data >= 16:
        return "OPCIONAL"
    elif 70 > data >= 18:
        return "OBRIGATÓRIO"
    else:
        return "OPCIONAL"



ano = (int(input("Digite o ano do seu nascimento: ")))
condicao_voto = voto(ano)
print(f"Você tem {data} anos de idade!")
print(f"Pelo seu ano de nascimento a sua indicação de voto é {condicao_voto}")