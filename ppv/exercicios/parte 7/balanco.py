def balanco(a):
    aberto = 0
    for i in a:
        if i == "(":
            aberto += 1
        elif i == ")":
            if aberto == 0:  
                return "incorrect"
            aberto -= 1
    
    if aberto == 0:
        return "correct"
    else:
        return "incorrect"

try:
    while True:
        a = input().strip()
        if a:  
            print(balanco(a))
except EOFError:
    pass
