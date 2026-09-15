class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)
        dp = [0] * (n + 1)
        pal = [bytearray(n) for _ in range(n)]

        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i < 2 or pal[i + 1][j - 1]):
                    pal[i][j] = 1

        last = -1
        ans = 0

        for end in range(n):
            dp[end + 1] = dp[end]

            for start in range(last + 1, end + 1):
                if end - start + 1 >= k and pal[start][end]:
                    ans += 1
                    last = end
                    break

        return ans