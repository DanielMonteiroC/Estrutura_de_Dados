#Escreva uma função que calcule o tempo necessário para cozinhar um ovo, sabendo que o tempo de cozimento para um ovo de tamanho médio é de 3 minutos e que cada ovo adicionado aumenta o tempo em 1 minuto.
def cozinhar_ovo(ovo_adcionar):   
    if ovo_adcionar <= 0:
        raise Exception("Assim sua refeição nunca ficará pronta.")
        
    else:
        panela = 3
        tempo_total = panela + (ovo_adcionar - 1)
        return tempo_total

ovo_adcionar = int(input("Coloque a quantidade desejada: "))
print(f"Sua refeição ficara pronta em {cozinhar_ovo(ovo_adcionar)} minutos!")


