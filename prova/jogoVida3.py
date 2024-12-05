N, Q  = [int(x) for x in input().split()]

#M = [[int(x) for x in input()] for i in range(N)]

M1 = [[0 for j in range(N)] for i in range(N)]
M2= [[0 for j in range(N)] for i in range(N)]

for i in range(N):
    linha =  input()
    for j in range(N):
        M1[i+1][j+1] = int(linha[j])

def calculaVizinhos(matriz, i, j):
    linha1 = matriz[i-1][j-1] + matriz[i-1][j] + matriz[i-1][j+1]
    linha2 = matriz[i][j-1] + matriz[i][j] + matriz[i][j+1]
    linha3 = matriz[i+1][j-1] + matriz[i+1][j] + matriz[i+1][j+1]
    return linha1 + linha2 + linha3

def calculaPasso(origem, destino):
    for i in range(1, N+1):
        for j in range(1, N+1):
            vizinhosVivos = calculaVizinhos(origem, i, j)

            if origem[i][j] == 1:
                if vizinhosVivos == 2 or vizinhosVivos == 3:
                    destino[i][j] = 1
                else:
                    destino[i][j] = 0
            else:
                if vizinhosVivos == 3:
                    destino[i][j] = 1
                else:
                    destino[i][j] = 0

MatrizFinal= 0
for passo in range(Q):
    if Q % 2 == 0:
        calculaPasso(M1, M2)
        MatrizFinal = M2
        
    else:
        calculaPasso(M2, M1)
        MatrizFinal = M1

#[[print(cada, end="") for cada in M1] for row in Q]

for i in range(1, N+1):
    for j in range(1, N+1):
        print(MatrizFinal[i][j], end="")
    print()