def solution(m, n, startX, startY, balls):
    import math
    answer = []
    def distance(x1, y1, x2, y2):
        return math.sqrt( math.pow(x1 - x2, 2) + math.pow(y1 - y2, 2))
    for endX, endY in balls:
            상,하,좌,우 = float('inf'),float('inf'),float('inf'),float('inf')
            if not (startX==endX and startY>endY):
                하 = distance(startX, -startY, endX, endY)
            if not (startX>endX and startY==endY):
                좌 = distance(-startX, startY, endX, endY)
            if not (startX==endX and startY<endY):
                상 = distance(startX, 2*n-startY, endX, endY)
            if not (startX<endX and startY==endY):
                우 = distance(2*m-startX, startY, endX, endY)
            answer.append(round(math.pow(min(상,하,좌,우),2)))
    return answer