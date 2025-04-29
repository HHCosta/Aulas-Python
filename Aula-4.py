from time import sleep
#Exercicio 1
# x = 1
# while x<=100:
#     print(x)
#     x=x+1

#Exercicio 2
# x = 50
# while x<=100:
#     print(x)
#     x=x+1
#Exercicio 3
# x = 10
# while x>=0:
#     if x>0:
#         print(x)
#         sleep(1)
#     x-=1
# else:
#     print(" e Fogo!")
# #Exercicio 4
# fim = int(input())
# x = 1
# while x<fim:
#     print(x)
#     x+=2
# #Exercicio 5
# x = 3
# y = 1
# while y<=10:
#     print(x)
#     x+=3
#     y+=1
#Exericio 6
# n = int(input("Tabuada"))
# x = 1
# while x<=10:
#     print(str(n) + "x" + str(x) +" = " + str(x*n))
#     x= x+1
#Exercicio 7
# x = int(input("Inico"))
# y = int(input("Fim"))
# n = int(input("tabuada"))
# while x<=y:
#     print(str(n) + "x" + str(x) + " = " + str(x * n))
#     x= x+1
# #Exercico 8
# VP = int(input())
# juros = (int(input())/100)
# x= 1
# while x<=24:
#     VP = VP + VP * juros
#     print(f"Soma = {VP:.2f}")
#     x+=1
# print(juros)
#Exercicio 9
VP = int(input())
juros = (int(input())/100)
x= 1
while x<=24:
    m= int(input("ganho mensal"))
    VP = VP + m
    VP = VP + VP * juros
    print(f"Soma = {VP:.2f}")
    x+=1
print(juros)