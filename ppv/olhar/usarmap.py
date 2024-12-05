#matriz multidimensional
turma = [[9.5, 9, 8, 0],
         [5, 6, 7, 8.5], 
         [9, 8, 8, 0], 
         [3.6, 7.0, 9.1, 8.7], 
         [5.0, 4.5, 7.0, 5.2], 
         [2.1, 6.5, 8.0, 7.0] ]

print(f"Impressão em formato linear:{turma}\n")
#impressão em formato de matriz: forma 1
for linha in range(6):
    for coluna in range(4):
        print(f"{turma[linha][coluna]} ", end='') #end é utilizado para remover a quebra de linha
    print()

print("\nSegundo exemplo formatada")
#impressão em formato de matriz: forma 2
for linha in turma:
        #converte cada elemento em uma string e junta com espaços
        print(' '.join(map(str, linha)))
        
        