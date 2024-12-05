
a = int(input())

for i in range(a):

    b = input()
    

    b = list(b.replace('.', ''))
    
    abre = 0  
    diamantes = 0 
    
    for j in b:
        if j == '<':
            abre += 1  
        elif j == '>' and abre > 0:
            abre -= 1 
            diamantes += 1  
    
   
    print(diamantes)
