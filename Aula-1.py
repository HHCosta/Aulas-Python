#d = True
#print(type(d))
#
# nota = 8
# media = 7
# aprovado = nota >= media
# print(aprovado)
#
# num1 = int(input("numero 1 "))
# num2 = int(input("numero 2 "))
# soma = num1 + num2
# print(soma)
#
# metro = int(input("escreva a distancia "))
# milimetro = metro * 1000
# print("em milimetro fica " + str(milimetro))
#
# dias = int(input("dias: "))
# horas = int(input("horas: "))
# segundos = int(input("segundos: "))
#
# dps = (dias * 24) * 60
# hps = horas * 60
# total = dps + hps + segundos
# print("total em segundos" + str(total))
#
# salario = int(input("coloque o salario"))
# porcentagem = int(input("coloque o numero da porcentagem"))
# aumento = (salario * (porcentagem/100)) + salario
# print("O salario com aumento sera " + str(aumento))
#

# valor = int(input("digite o valor"))
# desconto = int(input("digite o desconto"))
# preco_final = (valor*(desconto/100)) + valor
# print("O desconto era de " + str(desconto) + "% e o preço final ficou " + str(preco_final) + "R$")

distancia = int(input("digite a distancia em KM "))
velocidade = int(input("digite a velocidade em KM/H "))
tempo = distancia/velocidade
print("O tempo em horas é " + str(tempo))