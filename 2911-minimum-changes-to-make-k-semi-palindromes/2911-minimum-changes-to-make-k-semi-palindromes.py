class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)
        
        # Precompute proper divisors for every possible substring length
        divisors = [[] for _ in range(n + 1)]
        for d in range(1, n):
            for length in range(2 * d, n + 1, d):
                divisors[length].append(d)
                
        # cost[i][j] stores the min changes to make s[i:j+1] a semi-palindrome
        cost = [[float('inf')] * n for _ in range(n)]
        for i in range(n):
            for j in range(i + 1, n):
                length = j - i + 1
                min_c = float('inf')
                for d in divisors[length]:
                    c = 0
                    for rem in range(d):
                        left = i + rem
                        right = j - (d - 1 - rem)
                        while left < right:
                            if s[left] != s[right]:
                                c += 1
                            left += d
                            right -= d
                    if c < min_c:
                        min_c = c
                cost[i][j] = min_c
                
        # dp[p][i] stores min changes to partition s[:i] into p semi-palindromes
        dp = [[float('inf')] * (n + 1) for _ in range(k + 1)]
        dp[0][0] = 0
        
        for p in range(1, k + 1):
            # Each substring must have length at least 2
            for i in range(2 * p, n + 1):
                for prev in range(2 * (p - 1), i - 1):
                    if dp[p - 1][prev] != float('inf'):
                        dp[p][i] = min(dp[p][i], dp[p - 1][prev] + cost[prev][i - 1])
                        
        return dp[k][n]
