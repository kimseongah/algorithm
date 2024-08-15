def solution(board):
    from collections import deque
    answer = 0
    movements = [(-1,0),(1,0),(0,-1),(0,1)]
    start = (0,0)
    n = len(board)
    m = len(board[0])
    for i in range(n):
        board[i] = list(board[i])
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'R':
                start = (i, j)
    def bfs(a,b):
        q = deque([(a,b)])
        board[a][b] = 0
        while(q):
            a,b = q.popleft()
            for x, y in movements:
                na, nb = a+x, b+y
                while(na>=0 and nb>=0 and na<n and nb<m and board[na][nb]!='D'):
                    na, nb = na+x, nb+y
                na, nb = na-x, nb-y
                if board[na][nb] == 'G':
                    return board[a][b]+1
                if type(board[na][nb]) is not int and (na!=a or nb!=b):
                    board[na][nb] = board[a][b]+1
                    q.append((na,nb))
        return -1
    answer = bfs(start[0], start[1])
    return answer