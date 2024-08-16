def solution(citations):
    citations.sort()
    n = len(citations)
    answer = n-1
    for i in range(n):
        pivot = citations[i]
        if pivot >= n-i:
            answer = n-i
            return answer
    return 0