def solution(stones, k):
    def count_sequence(value):
        count = 0
        for s in stones:
            if s <= value:
                count += 1
            else:
                count = 0
            if count >= k:
                return False
        return True
    lo = min(stones)
    hi = max(stones)
    while lo < hi:
        mid = (lo + hi) // 2
        if count_sequence(mid):
            lo = mid + 1
        else:
            hi = mid
    return lo