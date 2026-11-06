from collections import defaultdict

class Solution:
    def countServers(self, n: int, logs: list[list[int]], x: int, queries: list[int]) -> list[int]:
        # Sort logs based on request time
        logs.sort(key=lambda log: log[1])
        
        # Keep track of original query indices by pairing them: (query_time, original_index)
        sorted_queries = sorted((q, i) for i, q in enumerate(queries))
        
        ans = [0] * len(queries)
        server_counts = defaultdict(int)
        active_servers = 0
        
        left = 0
        right = 0
        m = len(logs)
        
        for q_time, q_idx in sorted_queries:
            # Expand the window: include all logs that happen up to q_time
            while right < m and logs[right][1] <= q_time:
                server_id = logs[right][0]
                if server_counts[server_id] == 0:
                    active_servers += 1
                server_counts[server_id] += 1
                right += 1
                
            # Shrink the window: remove all logs that happen strictly before (q_time - x)
            while left < m and logs[left][1] < q_time - x:
                server_id = logs[left][0]
                server_counts[server_id] -= 1
                if server_counts[server_id] == 0:
                    active_servers -= 1
                left += 1
                
            # Total servers minus the ones that received at least one request
            ans[q_idx] = n - active_servers
            
        return ans
