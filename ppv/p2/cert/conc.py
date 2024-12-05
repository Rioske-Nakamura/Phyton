N, Q = [int(x) for x in input().split()	]

lista = [x for x in input().split()]
def test(cara, minI, maxI):
    if minI == maxI:
        return 0
    Nlista= lista[minI-1:maxI]
    conc = 0
    for x in range(len(Nlista)):
        for i in range(len(Nlista)):
            if x != i:
                conc += int(Nlista[x]+Nlista[i])
    return conc
for i in range(Q):
    L, R = [int(x) for x in input().split()    ]
    print(test(lista, L, R))