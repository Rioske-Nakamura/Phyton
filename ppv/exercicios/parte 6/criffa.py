abc= ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

n = int(input())

for i in range(n):
    frase = input()
    quantidade= int(input())
    frase0= ""
    for j in range(len(frase)):
        letras = abc.index(frase[j])
        letras -= quantidade

        if letras < -26:
            letras = letras % 26
        frase0 += abc[letras] 
    print(frase0)