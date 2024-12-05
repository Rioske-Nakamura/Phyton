mat1 = [[] for i in range(3)]

print(mat1)


mat2 = [[0 for j in range(3)] for i in range(4)]

for i in mat2:
    print(" ".join(map(str, i)))


#matriz multidimensional
mat3 = [[i*j for j in range(4)] for i in range(3)]

for i  in range(3):
    for j in range(4):
        print(f"{mat3[i][j]} ", end=" ")
    print()


#matriz dinamica

alunos = int(input("Quantos alunos: "))
notas = int(input("Quantas notas: "))


mat4 = [[[] for j in range(notas)] for i in range(alunos)]

for i in range(alunos):
    for j in range(notas):
        mat4[i][j] = int(input(f"Nota {j+1} do Aluno {i+1}: "))

for i in range(alunos):
    for j in range(notas):
        print(f"{mat4[i][j]} ", end=" ")
    print()