import datetime
pessoa = {}

pessoa["nome"] = input("Digite o seu nome: ")
pessoa["idade"] = ( datetime.date.today().year - int(input("Digite o seu ano de nascimento: ")))
Num_CLT = int(input("Digite o número da sua CLT, se não tiver digite 0 -> "))

if Num_CLT != 0:
    pessoa["ano_de_registro"] = int(input('Digite o ano da sua contratação: '))
    pessoa["salario"] = float(input("Digite o seu salário: "))
    pessoa["idade_aposentadoria"] = (35 - (datetime.date.today().year - pessoa["ano_de_registro"])) + pessoa["idade"]
else:
    pessoa["clt"] = "sem carteira"

print("-=" * 30)
for k ,v in pessoa.items():
    print(f'{k} tem o valor {v}')