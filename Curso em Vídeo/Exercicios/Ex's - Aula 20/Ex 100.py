from random import randint
import time


numeros = list()
qtd_num_sort = 5
def sorteia(numeros, qtd_num_sort):
    for i in range(0, qtd_num_sort):
        numeros.append(randint(0,10))
    somaPar(numeros)

def somaPar(numeros):
    print("-=" * 30)
    print("Os números da lista são: ", end="", flush=True)
    soma_par = 0
    for i in numeros:
        print(f"{i}..", end="", flush=True)
        time.sleep(0.5)
        if i % 2 == 0:
            soma_par += i
        else:
            pass
    print(f"\nA soma dos número pares da lista é: {soma_par}")
    numeros.clear()

sorteia(numeros, qtd_num_sort)
sorteia(numeros, qtd_num_sort)
sorteia(numeros, qtd_num_sort)
sorteia(numeros, qtd_num_sort)
sorteia(numeros, qtd_num_sort)