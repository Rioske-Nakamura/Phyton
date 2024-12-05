import time

inicio = time.time()

N = input()
B = list(map(int, input().split()))
f =0 
for i in B: 
    for j in B:
        if i-1 == j :
            i = j
            B.remove(j)
    f +=1

print(f)
fim = time.time()
print(fim - inicio)