def solution(money):
    dp = [0]*len(money)
    dp[0] = money[0]
    dp[1] = max(money[0], money[1])
    for i in range(2, len(money) - 1): #첫 번째 집 포함
        dp[i] = max(dp[i-1], dp[i-2]+money[i])
    a = dp[-2]
    dp[1] = money[1]
    dp[2] = max(money[1], money[2])
    for i in range(3, len(money)):
        dp[i] = max(dp[i-1], dp[i-2]+money[i])
    b = dp[-1]
    return max(a, b)