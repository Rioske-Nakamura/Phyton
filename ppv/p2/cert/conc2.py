N, Q = [int(x) for x in input().split()	]

lista = [x for x in input().split()]

for i in range(Q):
    L, R = [int(x) for x in input().split()    ]
    conc = 0
    if L != R:
        Nlista= lista[L-1:R]
        for x in range(len(Nlista)):
            for i in range(len(Nlista)):
                if x != i:
                    conc += int(Nlista[x]+Nlista[i])
    print(conc)