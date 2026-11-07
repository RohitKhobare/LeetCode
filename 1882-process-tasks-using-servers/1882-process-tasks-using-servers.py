import heapq

class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        ans = []
        
        free_servers = [(weight, idx) for idx, weight in enumerate(servers)]
        heapq.heapify(free_servers)
        
        busy_servers = []
        time = 0
        
        for task_idx, task_duration in enumerate(tasks):
            time = max(time, task_idx)
            
            if not free_servers and busy_servers[0][0] > time:
                time = busy_servers[0][0]
                
            while busy_servers and busy_servers[0][0] <= time:
                _, weight, idx = heapq.heappop(busy_servers)
                heapq.heappush(free_servers, (weight, idx))
                
            weight, idx = heapq.heappop(free_servers)
            ans.append(idx)
            heapq.heappush(busy_servers, (time + task_duration, weight, idx))
            
        return ans
