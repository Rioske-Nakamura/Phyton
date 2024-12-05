matriz1 = [[1,2,3, 4], 
           [4, 5, 6, 3], 
           [7, 8, 9, 11]]

matrizresult= [[[] for j in range(3)] for i in range(4)]




for i in range(4):
    for j in range(3):
        matrizresult[i][j] = matriz1[j][i]

for i in matrizresult:
    print(" ".join(map(str, i)))
print("n/")

#////////////////////////////////////////////////////////////////

matrizresult2= list(zip(*matriz1))
for i in matrizresult2:
    print(" ".join(map(str, i)))

print("n/")
#////////////////////////////////////////////////////////////////

matrizresult3= [[matriz1[j][i] for j in range(len(matriz1))] for i in range(len(matriz1[0]))]
for i in matrizresult3:
    print(" ".join(map(str, i)))


