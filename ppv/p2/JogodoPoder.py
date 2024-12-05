N, Q = [int(x) for x in input().split()	]

moster = []
for i in range(N):
    per = [int(x) for x in input().split()	]
    moster = moster + per


for i in range(N):
    for j in range(N):
        if i == N-1:
            if moster[j][i+1] < moster[j+1][i+1]:
                moster[j][i], moster[j+1][i+1] = moster[j][i+1], moster[j+1][i+1] + moster[j][i+1]
            else:
                moster[j][i+1] =  moster[j][i+1] + moster[j+1][i+1]

        if moster[j][i] < moster[j+1][i]:
            moster[j][i], moster[j+1][i] = moster[j][i], moster[j+1][i] + moster[j][i]
        else:
            moster[j][i] =  moster[j][i] + moster[j+1][i]
            
for i in range(moster):
   for j in range(len(moster[i])):
    moster[i].sort(reverse=True)
    print(moster[i][j], end ='')
   
