A = int(input())
N = [[[0 for x in range(A)] for x in range(A)] for x in range(A)]

A = A* A 

Lado1= 0
lado2 = 0
lado3 = 8



for i in range(A):
    for j in range(A):
        for k in range(A):
            if i == j and j == k:
                N[i][j][k] = 1

print(A)
print(N)