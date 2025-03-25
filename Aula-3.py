#1
velocidade = int(input("velocidade="))
if velocidade>80:
    ultra= velocidade - 80
    multa = 5 * ultra
    print("a multa foi de:")
    print(multa)

#2
primeiro = int(input("coloque o primeiro numero"))
segundo = int(input("coloque o segundo numero"))
terceiro = int(input("coloque o terceiro numero"))
if primeiro < segundo or primeiro < terceiro:
    print("O menor numero é")
    print(primeiro)
elif segundo < terceiro:
    print("O menor numero é")
    print(segundo)
else:
    print("O menor numero é")
    print(terceiro)

if primeiro > segundo & primeiro > terceiro:
    print("O maior numero é")
    print(primeiro)
elif segundo > terceiro:
    print("O maior numero é")
    print(segundo)
else:
    print("O maior numero é")
    print(terceiro)

#3
salario = int(input("Coloque o salario"))
if salario <= 1250:
    aumento = (salario * 0.15) + salario
    print("O salario aumentou para " + str(aumento))
else:
    aumento = (salario * 0.1) + salario
    print("O salario aumentou para " + str(aumento))


#4
distancia = int(input("Coloque a distancia"))
if distancia<=200:
    custo = 0.50 * distancia
    print(custo)
else:
    custo = 0.45 * distancia
    print(custo)

#5



