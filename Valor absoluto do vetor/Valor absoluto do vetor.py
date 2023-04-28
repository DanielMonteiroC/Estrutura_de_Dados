conjunto = [2/(3)**2, 81**0.5, 3**-1, -5, 10, 15]
soma = 0
for problema in conjunto:
    absoluto = abs(problema)
    soma += absoluto
    print(absoluto)
print("A soma dos valores absolutos da lista é:", soma)