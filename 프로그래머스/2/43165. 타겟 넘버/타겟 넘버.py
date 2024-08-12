def solution(numbers, target):
    answer = 0
    fin = []
    def dfs(v, result):
        if v+1 == len(numbers):
            fin.append(result + numbers[v])
            fin.append(result - numbers[v])
            return
        else:
            dfs(v+1, result+numbers[v])
            dfs(v+1, result-numbers[v])
    dfs(0, 0)
    for f in fin:
        if f == target:
            answer += 1
    return answer