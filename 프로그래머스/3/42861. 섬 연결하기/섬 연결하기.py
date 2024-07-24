def solution(n, costs):
    root = [i for i in range(n)]
    def get_root(index):
        if root[index]!= index:
            return get_root(root[index])
        return index
    def union(i1, i2):
        i1 = get_root(i1)
        i2 = get_root(i2)

        if i1 < i2:
            root[i2] = i1
        else:
            root[i1] = i2
    answer = 0
    costs.sort(key=lambda x: (x[2], x[0], x[1]))

    count = 0
    for edge in costs:
        if count == n-1:
            break
        a, b, cost = edge
        if get_root(a) != get_root(b):
            answer += cost
            count += 1
            union(a, b)

    return answer