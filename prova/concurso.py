N, K = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]
A.sort()
print(A[-K])