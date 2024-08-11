def solution(edges):
    answer = [0,0,0,0]
    indegree = [0]*1000000
    outdegree = [0]*1000000
    node_set = set()
    for a, b in edges:
        node_set.update({a, b})
        outdegree[a] += 1
        indegree[b] += 1

    # 8자 계산
    for i in node_set:
        if outdegree[i] == 2 and indegree[i] >= 2:
            answer[3] += 1

    # 만들어진 정점 찾기
    # 아무 그래프도 없었을 때
    num_node = len(node_set)
    if num_node == 1:
        answer[0] = 0
    else:
        for i in node_set:
            if indegree[i] == 0 and outdegree[i] >= 2:
                answer[0] = i
                break
    
    # bar 찾기
    for i in node_set:
        if outdegree[i] == 0:
            answer[2] += 1
    
    # 도넛 계산
    answer[1] = outdegree[answer[0]] - answer[2] - answer[3]

    return answer