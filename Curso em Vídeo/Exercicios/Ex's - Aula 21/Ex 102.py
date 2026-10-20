import time

fat = 1
num = int(input("Digite um número: "))
show = input("Deseja que o processo do fatorial apareça na tela? [S/N] -> ").strip().upper()[0]

if show in "S":
    show = True
else:
    show = False

def fatorial(num, show):
    print("-=" * 30)
    for i in range(1, num + 1):
        if show == True: print(f"{num} * {i}")
        if show == True: time.sleep(0.5)
        num *= i
    if show == True: print("-=" * 30)
    print(f"O valor do fatorial é {num}")

fatorial(num , show)
        


