a= 1
while a == 1:
    quant = int(input())
    if quant == 0:
        a = 0
        break
    z=1
    while z == 1:
        tudo = [int(x) for x in input().split()]

        b=0
        for j in range(len(tudo)):
            if tudo[0] == 0 :
                z=0
                print()
                break

            elif tudo[j] == j+1 or tudo[j] == quant -j:
                b+=1

            else:
                print("NO")
                break
        if b == len(tudo):
            print("YES")
        