class Solution:
    def climbStairs(self, n: int, costs: list[int]) -> int:
        # dp[i] will store the minimum cost to reach step i
        dp = [float('inf')] * (n + 1)
        dp[0] = 0  # Starting at step 0 has 0 cost
        
        # Iterate through each step from 1 to n
        for i in range(1, n + 1):
            # Check all possible jumps from previous steps (i-1, i-2, i-3)
            for prev in range(max(0, i - 3), i):
                jump_cost = costs[i - 1] + (i - prev) ** 2
                dp[i] = min(dp[i], dp[prev] + jump_cost)
                
        return dp[n]
