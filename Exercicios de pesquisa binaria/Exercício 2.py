# 2) Imagine um livro com páginas numeradas de 1 a 1000. Faça uma pesquisa binária para 
# encontrar uma página específica, seguindo as dicas de "maior" ou "menor" conforme você avança 
# nas páginas.

def pesquisa_binaria_pagina():
    inicio = 1
    fim = 1000
    tentativas = 0

    while inicio <= fim:
        meio = (inicio + fim) // 2
        tentativas += 1

        resposta = input(f"A página {meio} é a página que você está procurando? Digite 'm' para 'menor', 'M' para 'maior' e 'igual' se for a página correta: ")
        if resposta.lower() == "l":
            return meio, tentativas
        elif resposta.lower() == "p":
            fim = meio - 1
        elif resposta.lower() == "n":
            inicio = meio + 1
        else:
            print("Entrada inválida. Digite 'p' para 'menor', 'n' para 'maior' e 'l' se for a página correta.")

    return -1, tentativas

pagina_encontrada, num_tentativas = pesquisa_binaria_pagina()

if pagina_encontrada != -1:
    print(f"A página {pagina_encontrada} foi encontrada em {num_tentativas} tentativas!")
else:
    print("A página não foi encontrada.")