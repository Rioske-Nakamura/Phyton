N, Q = [int(x) for x in input().split()	]

ccara=  list(input())
teste= list(input())

certo= "S"

for i in range(Q):
    if teste[i] not in ccara:
        
        certo= "N"
        break

print(certo)