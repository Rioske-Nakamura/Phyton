N, Q = [int(x) for x in input().split()]

M = [[int(x) for x in input()] for j in range(N)]

MC = [L[:] for L in M]  

for k in range(Q):

    for i in range(N):
        for j in range(N):

            zero = 0

            if i > 0 and j > 0 and i < N - 1 and j < N - 1:
                zero += M[i][j + 1] == 1
                zero += M[i][j - 1] == 1

                zero += M[i + 1][j + 1] == 1
                zero += M[i + 1][j] == 1
                zero += M[i + 1][j - 1] == 1
                
                zero += M[i - 1][j + 1] == 1
                zero += M[i - 1][j] == 1
                zero += M[i - 1][j - 1] == 1

            else:
                if i == 0 and j == 0:
                    zero += M[i][j + 1] == 1
                    zero += M[i + 1][j + 1] == 1
                    zero += M[i + 1][j] == 1

                elif i == 0 and j == N - 1:
                    zero += M[i][j - 1] == 1
                    zero += M[i + 1][j - 1] == 1
                    zero += M[i + 1][j] == 1

                elif i == N - 1 and j == 0:
                    zero += M[i][j + 1] == 1
                    zero += M[i - 1][j + 1] == 1
                    zero += M[i - 1][j] == 1

                elif i == N - 1 and j == N - 1:
                    zero += M[i][j - 1] == 1
                    zero += M[i - 1][j - 1] == 1
                    zero += M[i - 1][j] == 1
                    
                elif i == 0:
                    zero += M[i][j - 1] == 1
                    zero += M[i][j + 1] == 1

                    zero += M[i + 1][j - 1] == 1

                    zero += M[i + 1][j] == 1
                    zero += M[i + 1][j + 1] == 1

                elif i == N - 1:
                    zero += M[i][j - 1] == 1
                    zero += M[i][j + 1] == 1

                    zero += M[i - 1][j - 1] == 1

                    zero += M[i - 1][j] == 1
                    zero += M[i - 1][j + 1] == 1

                elif j == 0:
                    zero += M[i - 1][j] == 1
                    zero += M[i + 1][j] == 1

                    zero += M[i - 1][j + 1] == 1
                    
                    zero += M[i][j + 1] == 1
                    zero += M[i + 1][j + 1] == 1

                elif j == N - 1:
                    zero += M[i - 1][j] == 1
                    zero += M[i + 1][j] == 1

                    zero += M[i - 1][j - 1] == 1

                    zero += M[i][j - 1] == 1
                    zero += M[i + 1][j - 1] == 1

            if M[i][j] == 0 and zero == 3:
                MC[i][j] = 1

            elif M[i][j] == 1 and (zero == 2 or zero == 3):
                MC[i][j] = 1

            else:
                MC[i][j] = 0

    M = [L[:] for L in MC]

for i in range(N):
    for j in range(N):
        print(MC[i][j], end=" ")
    print()
