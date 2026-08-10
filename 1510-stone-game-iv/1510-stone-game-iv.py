class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        # dp[i] indicates if the current player can win with i stones
        dp = [False] * (n + 1)
        
        for i in range(1, n + 1):
            k = 1
            # Check all perfect squares less than or equal to i
            while k * k <= i:
                if not dp[i - k * k]:
                    dp[i] = True
                    break  # Found a winning move, no need to check further
                k += 1
                
        return dp[n]
