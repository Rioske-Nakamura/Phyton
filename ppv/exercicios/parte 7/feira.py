N= int(input())

def sep (x):
    return x.split(" ")

for i in range(N):
    P = int(input())
    preco = {}   

    for j in range(P):
        item = input()
        Z = sep(item)
        preco[Z[0]] = float(Z[1])
    
    P = int(input())
    quant = 0
    for j in range(P):
        item = input()
        Z = sep(item)
    
        quant += preco[Z[0]] * float(Z[1])

    print(f"R$ {quant:.2f}")
    
