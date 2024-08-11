def solution(targets):
    answer = 0
    sorted_targets = sorted(targets, key=lambda x:x[1])
    covered = 0
    for a, b in sorted_targets:
        if covered <= a:
            answer += 1
            covered = b
    return answer