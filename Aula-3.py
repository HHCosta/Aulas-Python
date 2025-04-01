# #1
# velocidade = int(input("velocidade="))
# if velocidade>80:
#     ultra= velocidade - 80
#     print("Voce foi multado")
#     multa = 5 * ultra
#     print("a multa foi de:")
#     print(multa)
#
# #2
primeiro = float(input("coloque o primeiro numero"))
segundo = float(input("coloque o segundo numero"))
terceiro = float(input("coloque o terceiro numero"))
if primeiro < segundo and primeiro < terceiro:
    print("O menor numero é")
    print(primeiro)
elif segundo < terceiro:
    print("O menor numero é")
    print(segundo)
else:
    print("O menor numero é")
    print(terceiro)

if primeiro > segundo and primeiro > terceiro:
    print("O maior numero é")
    print(primeiro)
elif segundo > terceiro:
    print("O maior numero é")
    print(segundo)
else:
    print("O maior numero é")
    print(terceiro)

# #3
# salario = int(input("Coloque o salario"))
# if salario <= 1250:
#     aumento = (salario * 0.15) + salario
#     print("O salario aumentou para " + str(aumento))
# else:
#     aumento = (salario * 0.1) + salario
#     print("O salario aumentou para " + str(aumento))
#
#
# #4
# distancia = int(input("Coloque a distancia"))
# if distancia<=200:
#     custo = 0.50 * distancia
#     print(custo)
# else:
#     custo = 0.45 * distancia
#     print(custo)

#5
#
# num1 = int(input("num1"))
# num2 = int(input("num2"))
# Operacao = str(input("Coloque o simbolo da operacao"))
# if Operacao == "+":
#     print(num1+num2)
# elif Operacao == "*":
#     print(num1*num2)
# elif Operacao == "/":
#     print(num1/num2)
# elif Operacao == "-":
#     print(num1-num2)
#6
# salario = int(input("salario"))
# casa = int(input("casa"))
# anos = int(input("anos"))
# apm = anos * 12
# prestacao = casa/apm
# if prestacao < salario * 0.3:
#     print("aprovado")
# else:
#     print("reprovado")
#7
# kw = int(input("kw"))
# tipo = str(input("tipo"))
# if tipo == "R":
#     if kw < 500:
#         print(kw*0.4)
#     else:
#         print(kw*0.65)
# elif tipo == "C":
#     if kw < 1000:
#         print(kw*0.55)
#     else:
#         print(kw*0.6)
# else:
#     if kw < 5000:
#         print(kw*0.55)
#     else:
#         print(kw*0.6)
#8
# nota1 = int(input("n1"))
# nota2 = int(input("n2"))
# media = (nota1+nota2)/2
# if media < 6:
#     print("reprovado")
# if media >= 6:
#     print("aprovado")
#9
# nota1 = int(input("n1"))
# nota2 = int(input("n2"))
# media = int((nota1+nota2)/2)
# if media > 6:
#     print("aprovado")
# if media < 4:
#     print("reprovado")
# else:
#     print("exame")