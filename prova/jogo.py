def contar_vizinhos_vivos(matriz, x, y, N):
    # Lista de coordenadas relativas dos 8 vizinhos possíveis
    vizinhos = [(-1, -1), (-1, 0), (-1, 1), 
                (0, -1),         (0, 1), 
                (1, -1), (1, 0), (1, 1)]
    
    vivos = 0
    for dx, dy in vizinhos:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < N:
            vivos += matriz[nx][ny]
    
    return vivos

def jogo_da_vida(N, Q, matriz):
    for _ in range(Q):
        nova_matriz = [[0] * N for _ in range(N)]
        for i in range(N):
            for j in range(N):
                vivos = contar_vizinhos_vivos(matriz, i, j, N)
                if matriz[i][j] == 1:
                    if vivos == 2 or vivos == 3:
                        nova_matriz[i][j] = 1
                    else:
                        nova_matriz[i][j] = 0
                else:
                    if vivos == 3:
                        nova_matriz[i][j] = 1
                    else:
                        nova_matriz[i][j] = 0
        matriz = nova_matriz
    
    return matriz

# Leitura da entrada
N, Q = map(int, input().split())
matriz = []
for _ in range(N):
    linha = list(map(int, input().strip()))
    matriz.append(linha)

# Simulação do jogo da vida
resultado = jogo_da_vida(N, Q, matriz)

# Impressão do resultado
for linha in resultado:
    print(''.join(map(str, linha)))
