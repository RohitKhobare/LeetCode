from typing import List
import heapq

class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        graph = [[] for _ in range(n)]

        for u, v, w in edges:
            graph[u].append((v, w))

        INF = float('inf')
        dist = [[INF] * (k + 1) for _ in range(n)]

        # The starting node counts as the first character in its run.
        dist[0][1] = 0
        pq = [(0, 0, 1)]

        while pq:
            cost, u, run = heapq.heappop(pq)

            if cost != dist[u][run]:
                continue

            if u == n - 1:
                return cost

            for v, w in graph[u]:
                if labels[v] == labels[u]:
                    new_run = run + 1
                    if new_run > k:
                        continue
                else:
                    new_run = 1

                new_cost = cost + w

                if new_cost < dist[v][new_run]:
                    dist[v][new_run] = new_cost
                    heapq.heappush(pq, (new_cost, v, new_run))

        return -1