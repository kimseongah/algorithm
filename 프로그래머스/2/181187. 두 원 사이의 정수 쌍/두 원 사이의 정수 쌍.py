from math import ceil, floor, sqrt
def solution(r1, r2):
    answer = 0
    for i in range(1,r2+1):
        if i  < r1:
            answer += (floor(sqrt(r2*r2-i*i)) - ceil(sqrt(r1*r1-i*i))+1)
        else:
            answer += (floor(sqrt(r2*r2-i*i))+1)
    answer *=4
    return answer