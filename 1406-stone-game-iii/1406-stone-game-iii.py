class Solution:
    def stoneGameIII(self, stoneValue: list[int]) -> str:
        n = len(stoneValue)
        dp = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            current_sum = 0
            dp[i] = float("-inf")

            for take in range(3):
                if i + take >= n:
                    break

                current_sum += stoneValue[i + take]
                dp[i] = max(dp[i], current_sum - dp[i + take + 1])

        if dp[0] > 0:
            return "Alice"
        if dp[0] < 0:
            return "Bob"
        return "Tie"