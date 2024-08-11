def solution(picks, minerals):
    from collections import defaultdict
    answer = 0
    sums_of_five = defaultdict(lambda :0)
    for i, m in enumerate(minerals):
        if i >= sum(picks)*5:
            break
        index = i // 5
        if m == "diamond":
            minerals[i] = 25
        elif m == "iron":
            minerals[i] = 5
        elif m == "stone":
            minerals[i] = 1
        sums_of_five[index] += minerals[i]
    
    sorted_keys = sorted(sums_of_five, key=sums_of_five.get, reverse=True)

    for i in sorted_keys:
        if picks[0] > 0:
            picks[0] -= 1
            pick = 25
        elif picks[1] > 0:
            picks[1] -= 1
            pick = 5
        elif picks[2] > 0:
            picks[2] -= 1
            pick = 1
        else:
            break
        for j in range(5):
            index = 5 * i + j
            if index >= len(minerals):
                break
            if pick >= minerals[index]:
                answer += 1
            elif pick * 5 >= minerals[index]:
                answer += 5
            else:
                answer += 25
            
    return answer