#Exercicio 1
# notas = [0, 0, 0, 0, 0, 0, 0]
# soma = 0
# x = 0
# while x < 7:
#     notas[x] = float(input(f"Nota {x+1} = "))
#     soma += notas[x]
#     x += 1
# print(f"Média = {(soma/x):.2f}")
#Exercicio 2

# n = int(input())
# x1 = 0
# L1 = []
#
# while x1<n:
#     num = int(input("digite um numero"))
#     L1.append(num)
#     x1 = x1+1
#
#
#
# n = int(input())
# x2 = 0
# L2 = []
#
# while x2<(n):
#     num = int(input("digite um numero"))
#     L2.append(num)
#     x2 = x2 + 1
#
#
#
# L3 = []
# x3 = 0
#
# while x3<x1:
#     L3.append(L1[x3])
#     x3 = x3 + 1
#
#
# x3 = 0
# while x3<x2:
#     L3.append(L2[x3])
#     x3 = x3+1
# print(L3)
#Exercicio 3
# L = [15, 7, 27, 39]
# pesquisa = int(input("Digite o valor a pesquisar: "))
# x = 0
# while x < len(L):
#     if L[x] == pesquisa:
#         print(f"{pesquisa} achado na posição {x}.")
#         break
#     else:
#         achou = False
#         x += 1
# if x == 4:
#     print(f"{pesquisa} não encontrado.")
