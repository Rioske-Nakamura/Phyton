quant = int(input())
number = [[] for i in range(quant)]

for i in range(quant):
    alunos = int(input())    
    nomes = [x for x in input().split(" ")]
    presensa = [x for x in input().split(" ")]
    
    for j in range(alunos):
        falta = 0
        prensaca2= 0
    
        for k in range(len(presensa[j])):
            
            if presensa[j][k] == "A":
                falta += 1
            if presensa[j][k] == "M":
                    prensaca2 += 1
                    
        prensaca2 = len(presensa[j]) - prensaca2 
        
       
        if 100-(falta  * 100 / prensaca2) < 75: 
            number[i].append(nomes[j])
            

for i in range(quant):
    aprovados= ""
    for j in range(len(number[i])):
        if j == len(number[i]) - 1:
            aprovados += number[i][j]
        else:
            aprovados += number[i][j] + " "
    print(aprovados)