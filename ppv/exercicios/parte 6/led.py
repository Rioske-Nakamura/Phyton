quant = int(input())

todos = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]


for i in range(quant):
    tudo = input()
    k = 0
    for j in range(len(tudo)):
        p = int(tudo[j])
        k += todos[p]

    print(f"{k} leds" )
