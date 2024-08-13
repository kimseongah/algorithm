import sys

input = sys.stdin.readline

N = int(input())
A = [0] * (501)
for _ in range(N):
    index, value = map(int, input().split())
    A[index] = value
leng = max(A)

dp = [1] * (leng+1)

for i in range(2, leng+1):
    if A[i] == 0:
        continue
    for j in range(1, i):
        if A[j] == 0:
            continue
        if A[j] < A[i]:
            dp[i] = max(dp[i], dp[j]+1)

print(N-max(dp))