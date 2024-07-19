import sys
from bisect import bisect_left

input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))

LIS = [A[0]]

for item in A:
    if LIS[-1] < item:
        LIS.append(item)
    else:
        idx = bisect_left(LIS, item)
        LIS[idx] = item

print(len(LIS))