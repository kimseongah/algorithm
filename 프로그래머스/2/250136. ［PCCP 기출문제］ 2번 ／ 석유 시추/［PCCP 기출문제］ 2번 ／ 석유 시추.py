from collections import defaultdict
import sys
sys.setrecursionlimit(10 ** 6)

def solution(land):
    n = len(land)
    m = len(land[0])
    count = 2
    bulk = defaultdict(int)
    movements = [(-1,0),(1,0),(0,-1),(0,1)]
    def dfs(a, b):
        if land[a][b] == 1:
            land[a][b] = count
            bulk[count] += 1
            for movea, moveb in movements:
                na, nb = a + movea, b + moveb
                if na>=0 and nb >= 0 and na < n and nb < m:
                    dfs(na, nb)
        else:
            return
                    
    for i in range(n):
        for j in range(m):
            if land[i][j]==1:
                dfs(i,j)
                count += 1
    max_result = 0
    for j in range(m):
        cand = set()
        for i in range(n):
            if land[i][j] > 1:
                cand.add(land[i][j])
        amount = 0
        for index in cand:
            amount += bulk[index]
        if amount > max_result:
            max_result = amount
    return max_result