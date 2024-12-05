matriz= [[0 for j in range(5)] for i in range(5)]
soma=0
for i in range(5):
    for j in range(5):
        if i == j:
            matriz[i][j] = 1
            matriz[i][-j-1] = 1
        elif matriz[i][j] == 0:
            matriz[i][j] = 2
        


for i in range(5):
    print(" ".join(map(str, matriz[i])))

for i in range(5):
    for j in range(5):
        soma +=  matriz[i][j]
print(soma)