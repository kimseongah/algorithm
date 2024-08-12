def solution(n, computers):
    answer = 0
    visited = [False] * n
    def dfs(v):
        if not visited[v]:
            visited[v] = True
            for i, neighbor in enumerate(computers[v]):
                if neighbor == 1:
                    dfs(i)
                
    for i in range(n):
        if not visited[i]:
            answer += 1
            dfs(i)
    return answer