A =  input()

strg= ["zero","um", "dois", "tres", "quatro", "cinco", "seis", "sete","oito", "nove"]

if A.isalpha() == True:
    print(strg.index(A))
else:
    print(strg[int(A)])