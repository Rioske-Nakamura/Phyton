matriz1 = [[1,2,3], [4, 5, 6], [7, 8, 9]]
matriz2 = [[6,5,4], [3,2,1], [9,8,7]]

matriznova = [[[] for j in range(3)] for i in range(3)]

for i in range(3):
    for j in range(3):
        matriznova[i][j] = matriz1[i][j] + matriz2[i][j]

for i in matriznova:
    print(" ".join(map(str, i)))


#////////////////////////////////////////////////////////////////////////////////////
#////////////////////////////////////////////////////////////////////////////////////
matriznova = [[[] for j in range(3)] for i in range(3)]

matriznova = [[matriz1[i][j] + matriz2[i][j] for j in range(3)] for i in range(3)]

for i in matriznova:
    print(" ".join(map(str, i)))

#multiplicaçao de matrizes

matriz1 = [[3,2], [5,-1]]
matriz2 = [[6,4,-2], [0,7,1]]


matriznova = [[0 for j in range(len(matriz1[2]))] for i in range(len(matriz1))]


for i in range(len(matriz1)):
    for j in range(len(matriz1[2])):
        for k in range(len(matriz1[2])):
            matriznova[i][j] += matriz1[i][k] * matriz2[k][j]

for i in matriznova:
    print(" ".join(map(str, i)))