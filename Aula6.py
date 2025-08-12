# L = [8, 9, 15]
# for e in L:
#     print(e)
# for v in range(10):
#     print(v)
# L = [1, 2, 24, 4]
# maximo = L[0]
# for e in L:
#     if e > maximo:
#         maximo = e
# print(maximo)
#Exercicio 1
#
# L = [1, 2, 24, 4]
# minimo = L[0]
# for e in L:
#     if e < minimo:
#         minimo = e
# print(minimo)
#Exercicio 2
# T = [-10, -8, 0, 1, 2, 5, -2, -4]
# minimo = T[0]
# for e in T:
#     if e < minimo:
#         minimo = e
# print(minimo)
# maximo = T[0]
# for e in T:
#         if e > maximo:
#             maximo = e
# print(maximo)
#Exercicio 3
# V = [9, 8, 7, 12, 0, 13, 21]
# P = []
# I = []
# for e in V:
#      if e%2 == 0:
#         P.append(e)
#      else:
#         I.append(e)
# print(P)
# print(I)
#Exercicio 4
L = []
while True:
    x = input()
    if x == "fim":
        break
    L.append(x)
print(L)