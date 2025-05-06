
#Heitor Costa
x = 1

while x<3:
    print("Semestre " + str(x))
    CP1 = float(input("CP1 (nota entre 0 e 10)"))
    CP2 = float(input("CP2 (nota entre 0 e 10)"))
    CP3 = float(input("CP3 (nota entre 0 e 10)"))
    SP1 = float(input("SP1 (nota entre 0 e 10)"))
    SP2 = float(input("SP2 (nota entre 0 e 10)"))
    GS = float(input("GS (nota entre 0 e 10)"))
    if CP1 < CP2 and CP1 < CP3:
        menor = CP1
    elif CP2 < CP3:
        menor = CP2
    else:
        menor = CP3

    CPnota = CP1 + CP2 + CP3 - menor
    SPnota = SP1 + SP2
    mediaA = (SPnota + CPnota)/4
    nota1 = mediaA * 0.4
    nota2 = GS * 0.6
    notaTotal = nota1 + nota2
    if x == 1:
        S1 = notaTotal
    else:
        S2 = notaTotal
    x= x+1

Mfinal = (S1 * 0.4) + (S2 * 0.6)
print(f"A media final do aluno foi 5,6 {Mfinal:.1f}")
print(S1)
print(S2)
