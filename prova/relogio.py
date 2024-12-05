H = int(input())
M = int(input())
S = int(input())

T = int(input())

S = S + T
M = M + S//60
H = H + M//60
M = M%60
H = H%24
S = S%60

print(H)
print(M)
print(S)

