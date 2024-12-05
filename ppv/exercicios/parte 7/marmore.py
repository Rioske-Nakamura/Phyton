N , Q = 1, 2

def marmore(Z, P):
    for i in range(len(Z)):
        if Z[i] == P:
            return f"{P} found at {i + 1}"
    return f"{Q} not found"
caso =1
while True:
    N , Q = [int(x) for x in input().split()]
    if N == 0 and Q == 0:
        break
    Z  = []

    for i in range (N+Q):
        Z.append(int(input()))

    Z.sort()
    print(f"CASE# {caso}" )

    for i in range (Q):
        P = int(input())
        print(marmore(Z, P))
    caso +=1