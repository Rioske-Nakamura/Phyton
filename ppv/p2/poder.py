# Função para verificar se uma posição está dentro dos limites da matriz
def is_valid(x, y, N, M):
    return 0 <= x < N and 0 <= y < M

# Função DFS para calcular o poder máximo que pode ser alcançado a partir de uma célula
def dfs(x, y, grid, dp, N, M):
    # Se já calculamos o máximo poder para essa célula, retornar o valor armazenado
    if dp[x][y] != -1:
        return dp[x][y]
    
    # Poder inicial do herói
    max_power = grid[x][y]
    
    # Movimentos ortogonais: cima, baixo, esquerda, direita
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # Explorar todos os 4 movimentos
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if is_valid(nx, ny, N, M) and grid[nx][ny] <= max_power:
            # Se o herói pode derrotar o monstro na célula vizinha, fazemos a chamada recursiva
            max_power = max(max_power, grid[x][y] + dfs(nx, ny, grid, dp, N, M))
    
    # Armazenar o resultado na matriz de memorização
    dp[x][y] = max_power
    return max_power

# Função principal para ler a entrada e calcular o poder máximo para cada célula
def jogo_do_poder():
    # Ler a entrada
    N, M = map(int, input().split())
    grid = []
    for _ in range(N):
        grid.append(list(map(int, input().split())))
    
    # Matriz de memorização
    dp = []
    for i in range(N):
        dp.append([-1] * M)
    
    # Calcular o máximo poder para cada célula
    for i in range(N):
        for j in range(M):
            if dp[i][j] == -1:
                dfs(i, j, grid, dp, N, M)
    
    # Imprimir a saída
    for i in range(N):
        print(' '.join(str(dp[i][j]) for j in range(M)))

# Chamar a função principal
jogo_do_poder()
