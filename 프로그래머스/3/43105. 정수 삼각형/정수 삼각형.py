def solution(triangle):
    height = len(triangle)
    for i in range(1, height):
        for j in range(i+1):
            if j == 0:
                max_parent = triangle[i-1][j]
            elif j==i:
                max_parent = triangle[i-1][j-1]
            else:
                max_parent = max(triangle[i-1][j], triangle[i-1][j-1])
            triangle[i][j] = max_parent+triangle[i][j]
    answer = max(triangle[-1])
    return answer