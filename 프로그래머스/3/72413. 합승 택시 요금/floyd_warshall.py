INF = 1e8

def solution(n, s, a, b, fares):
    answer = INF
    graph = [[INF]*(n+1) for _ in range(n+1)]

    for start, end, f in fares:
        graph[start][end] = f
        graph[end][start] = f
    
    for k in range(n+1):
        for i in range(n+1):
            for j in range(n+1):
                graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])
    
    for x in range(1, n+1):
        graph[x][x] = 0
    
    for x in range(1, n+1):
        answer=min(graph[s][x]+graph[x][a]+graph[x][b], answer)

    return answer
