import heapq

class Solution:
    def minOperations(self, nums: list[int], x: int, k: int) -> int:
        n = len(nums)
        
        # Phase 1: Precompute the minimum cost for every window of size x
        cost = [0] * (n - x + 1)
        
        small = []  # Max-heap for the lower half (stores negative values)
        large = []  # Min-heap for the upper half
        
        left_sum = 0
        right_sum = 0
        left_size = 0
        right_size = 0
        
        deleted = set()
        pos = {}  # Tracks whether an active index is in 'left' or 'right' heap
        
        target_left = (x + 1) // 2
        
        def prune():
            while small and small[0][1] in deleted:
                heapq.heappop(small)
            while large and large[0][1] in deleted:
                heapq.heappop(large)
                
        def rebalance():
            nonlocal left_sum, right_sum, left_size, right_size
            prune()
            # Move from left to right if left has too many elements
            while left_size > target_left:
                val, idx = heapq.heappop(small)
                val = -val
                if idx in deleted:
                    continue
                heapq.heappush(large, (val, idx))
                left_sum -= val
                left_size -= 1
                right_sum += val
                right_size += 1
                pos[idx] = 'right'
                prune()
            
            # Move from right to left if left needs more elements
            while left_size < target_left and large:
                val, idx = heapq.heappop(large)
                if idx in deleted:
                    continue
                heapq.heappush(small, (-val, idx))
                right_sum -= val
                right_size -= 1
                left_sum += val
                left_size += 1
                pos[idx] = 'left'
                prune()

        # Build initial window
        for i in range(x):
            val = nums[i]
            if large and val > large[0][0]:
                heapq.heappush(large, (val, i))
                right_sum += val
                right_size += 1
                pos[i] = 'right'
            else:
                heapq.heappush(small, (-val, i))
                left_sum += val
                left_size += 1
                pos[i] = 'left'
            rebalance()
            
        prune()
        median = -small[0][0]
        cost[0] = (median * left_size - left_sum) + (right_sum - median * right_size)
        
        # Slide the window across the array
        for i in range(x, n):
            # Remove the element leaving the window
            out_idx = i - x
            out_val = nums[out_idx]
            deleted.add(out_idx)
            
            if pos[out_idx] == 'left':
                left_sum -= out_val
                left_size -= 1
            else:
                right_sum -= out_val
                right_size -= 1
            del pos[out_idx]
            
            prune()
            
            # Insert the new element entering the window
            in_val = nums[i]
            if large and in_val > large[0][0]:
                heapq.heappush(large, (in_val, i))
                right_sum += in_val
                right_size += 1
                pos[i] = 'right'
            else:
                heapq.heappush(small, (-in_val, i))
                left_sum += in_val
                left_size += 1
                pos[i] = 'left'
                
            rebalance()
            prune()
            median = -small[0][0]
            cost[i - x + 1] = (median * left_size - left_sum) + (right_sum - median * right_size)

        # Phase 2: Dynamic Programming to find k non-overlapping windows with minimum total cost
        dp = [[float('inf')] * (k + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            dp[i][0] = 0
            
        for i in range(1, n + 1):
            for j in range(1, k + 1):
                # Option 1: Skip the current element
                dp[i][j] = dp[i - 1][j]
                
                # Option 2: Form a subarray ending at index i-1 (starts at index i-x)
                if i >= x:
                    dp[i][j] = min(dp[i][j], dp[i - x][j - 1] + cost[i - x])
                    
        return dp[n][k]
