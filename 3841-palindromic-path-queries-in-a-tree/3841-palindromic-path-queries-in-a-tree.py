from typing import List

class Solution:
    def palindromePath(self, n: int, edges: List[List[int]], s: str, queries: List[str]) -> List[bool]:
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        parent = [-1] * n
        depth = [0] * n
        order = [0]
        parent[0] = 0

        for u in order:
            for v in graph[u]:
                if v != parent[u]:
                    parent[v] = u
                    depth[v] = depth[u] + 1
                    order.append(v)

        size = [1] * n
        heavy = [-1] * n

        for u in reversed(order):
            largest = 0
            for v in graph[u]:
                if parent[v] == u:
                    size[u] += size[v]
                    if size[v] > largest:
                        largest = size[v]
                        heavy[u] = v

        head = [0] * n
        pos = [0] * n
        timer = 0
        stack = [(0, 0)]

        while stack:
            u, h = stack.pop()
            while u != -1:
                head[u] = h
                pos[u] = timer
                timer += 1

                for v in graph[u]:
                    if parent[v] == u and v != heavy[u]:
                        stack.append((v, v))

                u = heavy[u]

        size_seg = 1
        while size_seg < n:
            size_seg <<= 1

        seg = [0] * (2 * size_seg)
        chars = list(s)

        for u in range(n):
            seg[size_seg + pos[u]] = 1 << (ord(chars[u]) - ord('a'))

        for i in range(size_seg - 1, 0, -1):
            seg[i] = seg[i * 2] ^ seg[i * 2 + 1]

        def update(u: int, c: str) -> None:
            chars[u] = c
            i = size_seg + pos[u]
            seg[i] = 1 << (ord(c) - ord('a'))
            i >>= 1
            while i:
                seg[i] = seg[i * 2] ^ seg[i * 2 + 1]
                i >>= 1

        def range_xor(left: int, right: int) -> int:
            result = 0
            left += size_seg
            right += size_seg

            while left < right:
                if left & 1:
                    result ^= seg[left]
                    left += 1
                if right & 1:
                    right -= 1
                    result ^= seg[right]
                left >>= 1
                right >>= 1

            return result

        def path_xor(u: int, v: int) -> int:
            result = 0

            while head[u] != head[v]:
                if depth[head[u]] < depth[head[v]]:
                    u, v = v, u

                result ^= range_xor(pos[head[u]], pos[u] + 1)
                u = parent[head[u]]

            if depth[u] > depth[v]:
                u, v = v, u

            result ^= range_xor(pos[u], pos[v] + 1)
            return result

        answer = []

        for query in queries:
            parts = query.split()

            if parts[0] == "update":
                update(int(parts[1]), parts[2])
            else:
                u, v = int(parts[1]), int(parts[2])
                mask = path_xor(u, v)
                answer.append((mask & (mask - 1)) == 0)

        return answer