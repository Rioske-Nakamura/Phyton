N, Q = [int(x) for x in input().split()]

moster = []
for i in range(N):
    per = [int(x) for x in input().split()]
    moster.append(per)

for i in range(N):
    moster[i].sort(reverse=True)


for i in range(N):
    for j in range(len(moster[i])):
        print(moster[i][j], end=' ')
    print()
