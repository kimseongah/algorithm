def solution(n):
    answer = [[0 for j in range(n)] for i in range(n)]
    x = y = 0
    count = 1
    dx = [0, 1, -1]
    dy = [1, 0, -1]
    d = 0
    while(True):
        answer[y][x] = count
        count += 1
        nx = x + dx[d]
        ny = y + dy[d]
        if nx == n or ny == n or answer[ny][nx] != 0:
            d = (d+1) % 3 #아래, 위, 대각선 순서대로 방향 전환
            nx = x + dx[d]
            ny = y + dy[d]
            if nx == n or ny == n or answer[ny][nx] != 0:
                break
        x = nx
        y = ny
    result = []
    for i in range(n+1):
        for j in range(i):
            result.append(answer[i-1][j])
    
    return result