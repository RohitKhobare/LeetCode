import heapq
from sortedcontainers import SortedList

class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        # Track number of handled requests per server
        request_count = [0] * k
        
        # All servers are initially available
        available = SortedList(range(k))
        
        # Min-heap to track busy servers: (free_time, server_id)
        busy = []
        
        for i, start_time in enumerate(arrival):
            # 1. Free up servers that finished their tasks before or at current arrival time
            while busy and busy[0][0] <= start_time:
                _, server_id = heapq.heappop(busy)
                available.add(server_id)
                
            # 2. If no servers are available, the request is dropped
            if not available:
                continue
                
            # 3. Find the ideal server using wrap-around lookup logic
            target = i % k
            idx = available.bisect_left(target)
            
            # If no server >= target, wrap around to the first available server
            if idx == len(available):
                idx = 0
                
            assigned_server = available.pop(idx)
            
            # 4. Update state configurations
            request_count[assigned_server] += 1
            heapq.heappush(busy, (start_time + load[i], assigned_server))
            
        # Find the server(s) with the highest processed request count
        max_requests = max(request_count)
        return [server_id for server_id, count in enumerate(request_count) if count == max_requests]
