import sys
import bisect

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

LIS = [A[0]]

for item in A:
    if LIS[-1] < item:
        LIS.append(item)
    else:
        index = bisect.bisect_left(LIS, item)
        LIS[index] = item
print(len(LIS))