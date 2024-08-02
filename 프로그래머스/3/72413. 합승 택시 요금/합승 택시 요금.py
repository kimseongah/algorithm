import heapq
INF = 1000001

def dijkstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q,[start,0])

    while q:
        now, dist = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for n,c in graph[now]:
            cost = c + dist
            if cost < distance[n]:
                distance[n] = cost
                heapq.heappush(q,[n,cost])
    return distance
def solution(n, s, a, b, fares):
    answer = 0
    global graph, distance
    graph = [[] for _ in range(n+1)]
    distance = [INF] * (n+1)
    min = 10**9
    for f in fares:
        graph[f[0]].append([f[1],f[2]])
        graph[f[1]].append([f[0],f[2]])
    d1 = dijkstra(s)
    for i in range(1,n+1):
        distance = [INF] * (n+1)
        d2 = dijkstra(i)
        if min > d2[a] + d2[b] + d1[i]:
            min = d2[a] + d2[b] + d1[i]
            # print(d2[a],d2[b],d1[i],i)

    return min