def solution(maps):
    from collections import deque
    answer= 0
    movement = [(-1,0),(1,0),(0,-1),(0,1)]
    v = len(maps)
    w = len(maps[0])
    q = deque([[0,0]])
    maps[0][0] += 1
    while q:
        cy, cx = q.popleft()
        for i in range(4):
            ny = cy + movement[i][0]
            nx = cx + movement[i][1]
            if ny < 0 or nx < 0 or ny >= v or nx >= w:
                continue
            else:
                if maps[ny][nx] == 1 :
                    maps[ny][nx] = maps[cy][cx] + 1
                    q.append([ny, nx])
    if maps[v-1][w-1] == 1:
        return -1
    else:
        return maps[v-1][w-1]-1