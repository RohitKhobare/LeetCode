from typing import List

class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        n = len(stoneValue)

        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + stoneValue[i]

        dp = [[0] * n for _ in range(n)]
        max_left = [[0] * n for _ in range(n)]
        max_right = [[0] * n for _ in range(n)]

        for i in range(n):
            max_left[i][i] = stoneValue[i]
            max_right[i][i] = stoneValue[i]

        for length in range(2, n + 1):
            for left in range(n - length + 1):
                right = left + length - 1

                lo, hi = left, right - 1

                while lo <= hi:
                    mid = (lo + hi) // 2

                    left_sum = prefix[mid + 1] - prefix[left]
                    right_sum = prefix[right + 1] - prefix[mid + 1]

                    if left_sum <= right_sum:
                        lo = mid + 1
                    else:
                        hi = mid - 1

                split = hi

                best = 0

                if split >= left:
                    left_sum = prefix[split + 1] - prefix[left]
                    best = max(best, max_left[left][split])

                    if left_sum == prefix[right + 1] - prefix[split + 1]:
                        best = max(best, max_right[split + 1][right])

                if split + 1 <= right - 1:
                    best = max(best, max_right[split + 2][right])

                dp[left][right] = best

                total = prefix[right + 1] - prefix[left]

                max_left[left][right] = max(
                    max_left[left][right - 1],
                    total + dp[left][right]
                )

                max_right[left][right] = max(
                    max_right[left + 1][right],
                    total + dp[left][right]
                )

        return dp[0][n - 1]