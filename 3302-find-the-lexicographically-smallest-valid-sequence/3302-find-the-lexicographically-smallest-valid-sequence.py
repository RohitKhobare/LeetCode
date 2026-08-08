class Solution:
    def validSequence(self, word1: str, word2: str) -> list[int]:
        n, m = len(word1), len(word2)
        
        # dp[i] stores the furthest index in word2 that can be matched 
        # using a suffix of word1 starting from index i.
        dp = [0] * (n + 1)
        j = m - 1
        
        # Precompute the suffix matching array from right to left
        for i in range(n - 1, -1, -1):
            if j >= 0 and word1[i] == word2[j]:
                j -= 1
            dp[i] = j + 1
            
        ans = []
        j = 0
        changed = False
        
        # Greedily match from left to right
        for i in range(n):
            if j == m:
                break
                
            # Case 1: Exact match
            if word1[i] == word2[j]:
                ans.append(i)
                j += 1
            # Case 2: Mismatch, but we can safely use our 1-character modification
            elif not changed and dp[i + 1] <= j + 1:
                ans.append(i)
                j += 1
                changed = True
                
        return ans if len(ans) == m else []
