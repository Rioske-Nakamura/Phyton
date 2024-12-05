matriz1 = [[1,2,3], [4, 5, 6]]



for i in range(len(matriz1)):
    for j in range(len(matriz1[0])):
        if matriz1[i][j]%2 == 0:
            matriz1[i][j] = matriz1[i][j] *3
       

for i in matriz1:
    print(" ".join(map(str, i)))