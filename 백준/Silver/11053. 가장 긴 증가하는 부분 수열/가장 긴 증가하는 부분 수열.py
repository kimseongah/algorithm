n = int(input())
A = list(map(int, input().split()))

dp = [0]*n

for i in range(n):
    for j in range(i):
        if A[j] < A[i]:
            dp[i] = max(dp[i], dp[j]+1)
    if dp[i] == 0:
        dp[i] = 1

print(max(dp))