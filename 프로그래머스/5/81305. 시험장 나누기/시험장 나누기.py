import sys
sys.setrecursionlimit(10 ** 6)

class test_room:
    def __init__(self, num, links):
        self.w = num
        n = len(links)
        self.maps = [[] for _ in range(n)]  # graph
        self.tree = [[] for _ in range(n)]
        self.cnt = 0
        amount = 0

        for idx, (a, b) in enumerate(links):
            if a != -1:
                self.maps[idx].append(a)
                self.maps[a].append(idx)
                amount += a
            if b != -1:
                self.maps[idx].append(b)
                self.maps[b].append(idx)
                amount += b

        self.root = (n - 1) * n // 2 - amount  # 루트 노드 계산
        self.make_tree(-1, self.root)

    def make_tree(self, pre, curr):
        for c in self.maps[curr]:
            if c != pre:
                self.tree[curr].append(c)
                self.make_tree(curr, c)

    def find(self, idx, value):
        if len(self.tree[idx]) == 0:  # 자식 없음
            return self.w[idx]
        else:
            l = self.find(self.tree[idx][0], value)
            r = 0 if len(self.tree[idx]) == 1 else self.find(self.tree[idx][1], value)
            if l + r + self.w[idx] <= value:
                return l + r + self.w[idx]
            else:
                self.cnt += 1
                if l <= r:
                    if l + self.w[idx] > value:
                        self.cnt += 1
                        return self.w[idx]
                    else:
                        return l + self.w[idx]
                else:
                    if r + self.w[idx] > value:
                        self.cnt += 1
                        return self.w[idx]
                    else:
                        return r + self.w[idx]

def solution(k, num, links):
    room = test_room(num, links)

    hi = sum(num)
    lo = max(num)

    while lo <= hi:
        mid = (lo + hi) // 2
        room.find(room.root, mid)
        if room.cnt > k - 1:
            lo = mid + 1
        else:
            hi = mid - 1
        room.cnt = 0

    return lo
