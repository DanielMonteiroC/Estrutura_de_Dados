# 1) Dado um jogo de adivinhação onde você precisa descobrir um número de 1 a 100, 
# faça uma pesquisa binária para emcontrar o numero com o menor número possivel de 
# tentativas.

def pesquisa_binaria(numero):
    inicio = 1
    fim = 100
    tentativas = 0

    while inicio <= fim:
        meio = (inicio + fim) // 2
        tentativas += 1

        if meio == numero:
            return meio, tentativas
        elif meio < numero:
            inicio = meio + 1
        else:
            fim = meio - 1

    return -1, tentativas

numero_desejado = int(input("Digite o número que deseja encontrar (entre 1 e 100): "))
numero_encontrado, num_tentativas = pesquisa_binaria(numero_desejado)

if numero_encontrado != -1:
    print(f"O número {numero_encontrado} foi encontrado em {num_tentativas} tentativas!")
else:
    print("O número não foi encontrado.")
