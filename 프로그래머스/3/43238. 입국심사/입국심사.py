def solution(n, times):
    lo = 1
    hi = min(times) * n
    while lo < hi:
        mid = (lo + hi) // 2
        count = 0
        for t in times:
            count += mid // t
        if count < n:
            lo = mid +1
        else:
            hi = mid
    return lo