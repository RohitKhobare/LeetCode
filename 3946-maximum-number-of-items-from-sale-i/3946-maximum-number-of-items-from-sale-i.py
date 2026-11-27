from collections import Counter

class Solution:
    def maximumSaleItems(self, items: list[list[int]], budget: int) -> int:
        max_f = max(f for f, _ in items)
        freq = Counter(f for f, _ in items)
        
        multiples = [0] * (max_f + 1)
        for f in range(1, max_f + 1):
            if freq[f] > 0:
                for m in range(f, max_f + 1, f):
                    multiples[f] += freq[m]
                multiples[f] -= 1
                
        min_price = min(p for _, p in items)
        
        dp = [0] * (budget + 1)
        for f, p in items:
            if p > budget:
                continue
            gain = 1 + multiples[f]
            for b in range(budget, p - 1, -1):
                if dp[b - p] + gain > dp[b]:
                    dp[b] = dp[b - p] + gain
                    
        ans = 0
        for b in range(budget + 1):
            extra = (budget - b) // min_price
            ans = max(ans, dp[b] + extra)
            
        return ans
