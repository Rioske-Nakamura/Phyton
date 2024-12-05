N, M = map(int, input().split())

poderes = []
for _ in range(N):
    linha = list(map(int, input().split()))
    poderes.append(linha)

dp = [[0 for _ in range(M)] for _ in range(N)]

for j in range(M):
    dp[0][j] = poderes[0][j]

for i in range(1, N):
    for j in range(M):
        for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            if 0 <= i + di < N and 0 <= j + dj < M:
           
                if dp[i][j] >= poderes[i + di][j + dj]:
                 
                    dp[i][j] = max(dp[i][j], dp[i + di][j + dj] + poderes[i][j])


for i in range(N):
    for j in range(M):
        print(dp[i][j], end=" ")
    print()
