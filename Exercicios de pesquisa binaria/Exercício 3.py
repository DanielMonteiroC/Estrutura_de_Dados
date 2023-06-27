# 3) Em um jogo de cartas, onde você precisa encontrar a carta "Ás de Espadas" em um baralho
# de 52 cartas, faça uma pesquisa binária para encontrar a posição da carta desejada. 

# Naipe de Espadas: Ás, 2, 3, 4, 5, 6, 7, 8, 9, 10, Valete(J), Dama(Q) e Rei(K).
# Naipe de Copas: Ás, 2, 3, 4, 5, 6, 7, 8, 9, 10, Valete(J), Dama(Q) e Rei(K).
# Naipe de Paus: Ás, 2, 3, 4, 5, 6, 7, 8, 9, 10, Valete(J), Dama(Q) e Rei(K).
# Naipe de Ouros: Ás, 2, 3, 4, 5, 6, 7, 8, 9, 10, Valete(J), Dama(Q) e Rei(K).


import random

def pesquisa_binaria(lista, valor_procurado):
    inicio = 0
    fim = len(lista) - 1
    tentativas = 0

    while inicio <= fim:
        meio = (inicio + fim) // 2
        tentativas += 1

        if lista[meio] == valor_procurado:
            return meio, tentativas
        elif lista[meio] < valor_procurado:
            inicio = meio + 1
        else:
            fim = meio - 1

    return -1, tentativas

naipes = ['espadas', 'copas', 'paus', 'ouros']
valores = ['Ás', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

posicao_as_espadas = -1
num_tentativas_total = 0
while posicao_as_espadas == -1:
    baralho = []
    for naipe in naipes:
        for valor in valores:
            baralho.append((valor, naipe))
    random.shuffle(baralho)

    for i, naipe in enumerate(naipes):
        lista_naipe = [carta[0] for carta in baralho if carta[1] == naipe]
        posicao, num_tentativas = pesquisa_binaria(lista_naipe, 'Ás')
        num_tentativas_total += num_tentativas

        if posicao != -1:
            posicao_as_espadas = i * len(lista_naipe) + posicao
            break

if posicao_as_espadas != -1:
    print(f"O 'Ás de Espadas' está na posição {posicao_as_espadas} do baralho, encontrado em {num_tentativas_total} tentativas!")
else:
    print("O 'Ás de Espadas' não foi encontrado.")
