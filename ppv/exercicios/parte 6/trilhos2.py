a= 1
while a == 1:
    quant = int(input())
    if quant == 0:
        a = 0
        break
    z=1
    while z == 1:
        tudo = [int(x) for x in input().split()]

        
        if tudo[0] == 0 :
            z=0
            print()
            break

        elif  tudo[-1] == 1 and tudo[0] == quant: 
            print("YES")
        elif tudo[0] == 1 and tudo[-1] == quant : 
            print("YES")
        else:
            print("NO")

            
        