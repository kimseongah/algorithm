def solution(N, number):
    from collections import defaultdict
    dp = defaultdict(set)
    dp[1].add(N)
    if number == N:
        return 1
    def get_unioned_set(a, b): 
        result = set()
        for n1 in dp[a]:
            for n2 in dp[b]:
                result.update({n1+n2, n1-n2, n2-n1, n1*n2})
                if n1 != 0:
                    result.add(n2//n1)
                if n2 != 0:
                    result.add(n1//n2)
        return result
    for k in range(2,9):
        dp[k].add(int(str(N)*k))
        for i in range(1, k):
            unioned_set = get_unioned_set(i, k-i)
            dp[k].update(unioned_set)
        if number in dp[k]:
            return k
    return -1