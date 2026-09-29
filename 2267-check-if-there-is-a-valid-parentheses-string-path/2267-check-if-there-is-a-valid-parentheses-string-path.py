class Solution:
    def hasValidPath(self, grid: List[List[str]]) -> bool:
        m, n = len(grid), len(grid[0])

        if (m + n) % 2 == 0 or grid[0][0] == ')' or grid[m - 1][n - 1] == '(':
            return False

        dp = [[set() for _ in range(n)] for _ in range(m)]
        dp[0][0].add(1)

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue

                prev = set()

                if i > 0:
                    prev |= dp[i - 1][j]
                if j > 0:
                    prev |= dp[i][j - 1]

                for bal in prev:
                    new_bal = bal + (1 if grid[i][j] == '(' else -1)
                    if new_bal >= 0:
                        dp[i][j].add(new_bal)

        return 0 in dp[m - 1][n - 1]