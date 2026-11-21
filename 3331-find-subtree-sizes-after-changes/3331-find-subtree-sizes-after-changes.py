import sys

sys.setrecursionlimit(200000)

class Solution:
    def findSubtreeSizes(self, parent: list[int], s: str) -> list[int]:
        n = len(parent)
        adj = [[] for _ in range(n)]
        for i in range(1, n):
            adj[parent[i]].append(i)
            
        new_parent = list(parent)
        last_seen = {}
        
        def dfs_reparent(u: int):
            char = s[u]
            prev_ancestor = last_seen.get(char, -1)
            if prev_ancestor != -1:
                new_parent[u] = prev_ancestor
                
            last_seen[char] = u
            for v in adj[u]:
                dfs_reparent(v)
            last_seen[char] = prev_ancestor
            
        dfs_reparent(0)
        
        new_adj = [[] for _ in range(n)]
        for i in range(1, n):
            new_adj[new_parent[i]].append(i)
            
        ans = [1] * n
        def dfs_size(u: int) -> int:
            for v in new_adj[u]:
                ans[u] += dfs_size(v)
            return ans[u]
            
        dfs_size(0)
        return ans
