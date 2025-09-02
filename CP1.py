CP = [0.0, 0.0, 0.0]
GS = [0.0]
SP = [0.0, 0.0]
x=0
mediaS1 = 0
mediaS2 = 0
while x < 2:
    print("Semestre",x+1)
    z = 0
    for e in CP:
        print("nota da CP",z+1)
        CP[z] = float(input())
        z += 1

    z = 0
    for t in GS:
        print("nota da GS",z+1)
        GS[z] = float(input())
        z += 1

    z = 0
    for s in SP:
        print("nota da SP",z+1)
        SP[z] = float(input())
        z += 1

    soma = sum(CP) - min(CP)
    mediaSCP = ((soma + sum(SP))/4) * 0.4
    mediaGS = GS[0] * 0.6
    mediaS = mediaGS + mediaSCP
    if x == 0:
        mediaS1 = mediaS * 0.4
    else:
        mediaS2 = mediaS * 0.6
    x += 1

mediaT = mediaS2 + mediaS1
print(f"A media final do aluno foi: {mediaT:.1f}")
