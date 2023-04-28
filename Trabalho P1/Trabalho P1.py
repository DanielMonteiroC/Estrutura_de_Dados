import time                          #Importa funcionalidade para medir tempo de execução do código
import matplotlib.pyplot as plt      #Importa biblioteca para gerar graficos e visualizações

elementos = [['a', 'b', 'c', 'd'],['q', 'i', 'n', 'm'],['f', 'e', 'h', 'j'],['p', 'o', 'l','g']]    #Cria uma lista chamada elementos.
lista1 = []    #Cria uma lista vazia que vai receber os elementos da lista elementos.
for sublista1 in elementos:    #Percorre a a lista elementos adcionando cada elemento a lista lista1.
    for item in sublista1:
        lista1.append(item)

for i in range(len(lista1)):    #Ordena a lista1 em ordem crescente usando o bubble sort¹
    for j in range(len(lista1)-1-i):
        if lista1[j] > lista1[j+1]:
            lista1[j], lista1[j+1] = lista1[j+1], lista1[j]

print("crescente:", lista1)    #Exibe a lista1 em ordem crescente

for i in range(len(lista1)):    #Ordena a lista1 em ordem decrescente usando o Bubble sort¹
    for j in range(len(lista1)-1-i):
        if lista1[j] < lista1[j+1]:
            lista1[j], lista1[j+1] = lista1[j+1], lista1[j]

print("decrescente:", lista1)    #Exibe a lista1 em ordem decrescente

ns = []    #Cria uma lista chamada ns que armazena os valores do gráfico.
tempos = []    #Cria uma lista chamada tempos de execução.

for n in range(1, 16):    #Executa um loop de 1 a 15 medindo o tempo de execução e armazenando os dados.
    start = time.perf_counter()    #Armazena o tempo inicial.
    end = time.perf_counter()    #Armazena o tempo final.
    ms = (end-start) * 10**6    #Armazena o tempo de execução.
    ns.append(n)
    tempos.append(ms)
print(start)    #Exibe os tempos.
print(end)
print(ms)

#plt.plot(ns, tempos)    #Gera e exibe o gráfico.
#plt.xlabel('Valor de n')
#plt.ylabel('Tempo de execução (micro segundos)')
#plt.show()

#¹ O bubble sort realiza múltiplas passagem por uma lista.
#Ele compara itens adjacentes e troca aqueles que estão fora de ordem.
#Cada passagem pela lista coloca o próximo maior valor na sua posição correta.
#Em essência, cada item se desloca como uma “bolha” para a posição à qual pertence.
