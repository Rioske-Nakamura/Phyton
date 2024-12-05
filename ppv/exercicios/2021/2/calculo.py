A = int(input())
B = int(input())
C = int(input())

result= 0
for i in range(B,C+1):
    V = str(i) 
    V = list(V)

    soma=0
    for j in range(len(V)):
        soma += int(V[j])
    
    if soma == A:
        result += 1
print(result)

