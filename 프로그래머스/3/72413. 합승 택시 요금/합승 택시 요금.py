from heapq import heappush, heappop
INF = 1e8

def dijkstra(start, n):
        heap = []
        distance = [INF] * (n+1)
        distance[start] = 0
        heappush(heap, [0, start])
        while heap:
            dist, node = heappop(heap)
            if distance[node] < dist:
                continue
            for no, c in links[node]:
                cost = c+dist
                if cost < distance[no]:
                    distance[no] = cost
                    heappush(heap, [cost, no])
        return distance

def solution(n, s, a, b, fares):
    answer = INF
    global links
    links = [[] for _ in range(n+1)]
    for start, end, fare in fares:
        links[start].append([end, fare])
        links[end].append([start, fare])
    distance_from_s = dijkstra(s, n)
    distance_from_a = dijkstra(a, n)
    distance_from_b = dijkstra(b, n)

    for i in range(1, n+1):
        cost = distance_from_s[i]+distance_from_a[i]+distance_from_b[i]
        if answer>cost:
            answer = cost
    return answer