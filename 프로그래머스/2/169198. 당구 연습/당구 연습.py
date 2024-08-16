import math

# 점과 점 사이의 거리 구하는 함수
def 두점사이의거리(x1, y1, x2, y2):
    result = math.sqrt( math.pow(x1 - x2, 2) + math.pow(y1 - y2, 2))
    return result


def 답구하기(startX, startY, endX, endY, m, n):
    상,하,좌,우 = float('inf'),float('inf'),float('inf'),float('inf')
    if not (startX==endX and startY>endY):
        하 = 두점사이의거리(startX, -startY, endX, endY)
    if not (startX>endX and startY==endY):
        좌 = 두점사이의거리(-startX, startY, endX, endY)
    if not (startX==endX and startY<endY):
        상 = 두점사이의거리(startX, 2*n-startY, endX, endY)
    if not (startX<endX and startY==endY):
        우 = 두점사이의거리(2*m-startX, startY, endX, endY)
    return round(math.pow(min(상,하,좌,우),2))

def solution(m, n, startX, startY, balls):
    answer=[답구하기(startX, startY, endX, endY, m, n) for endX, endY in balls]
    return answer