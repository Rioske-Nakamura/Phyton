N, Q = [int(x) for x in input().split()]

M = [[int(x) for x in input()] for _ in range(N)]

for _ in range(Q):
    MC = [row[:] for row in M] 

    for i in range(N):
        for j in range(N):
            zero = 0
            

            if i > 0:
                if M[i-1][j] == 1:
                    zero += 1
                if j > 0 and M[i-1][j-1] == 1:
                    zero += 1
                if j < N-1 and M[i-1][j+1] == 1:
                    zero += 1
            if i < N-1:
                if M[i+1][j] == 1:
                    zero += 1
                if j > 0 and M[i+1][j-1] == 1:
                    zero += 1
                if j < N-1 and M[i+1][j+1] == 1:
                    zero += 1
            if j > 0 and M[i][j-1] == 1:
                zero += 1
            if j < N-1 and M[i][j+1] == 1:
                zero += 1

     
            if M[i][j] == 0 and zero == 3:
                MC[i][j] = 1
            elif M[i][j] == 1 and (zero < 2 or zero > 3):
                MC[i][j] = 0

    M = [row[:] for row in MC] 

for i in range(N):
    for j in range(N):
        print(MC[i][j], end=" ")
    print()
