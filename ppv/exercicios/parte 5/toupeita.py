salas, tuneis = [int(x) for x in input().split()]

matriz = [[] for i in range(salas+1)]


for i in range(tuneis):
    entrada1, entrada2 = [int(x) for x in input().split()]

    matriz[entrada1-1].append(entrada2)
    matriz[entrada2-1].append(entrada1)

caminhos = int(input())
certo=0
for i in range( caminhos):
    entrada1 = [int(x) for x in input().split()]

    for j in range(entrada1[0]-1):
        print(entrada1[j+1])
        if entrada1[j+1] not in matriz[entrada1[j+1]]:
            print(0)
            break
    certo +=1
print(certo)
print(matriz)