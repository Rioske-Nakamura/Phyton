A =  int(input())
B =  [int(x) for x in input().split()]




def palindromo(N, M, S):
    soma =0 
    for i in range(N-S):
        if M[i] != M[-1-i]:
            soma +=1
    return soma
if A%2 != 0:
    
    print(palindromo(A, B, 3))    
else:
    print(palindromo(A, B, 2))

