class Solution:
    def smallestUniqueSubarray(self, nums: list[int]) -> int:
        n = len(nums)
        
        def has_unique(length: int) -> bool:
            seen_once = set()
            seen_twice = set()
            
            MOD1, BASE1 = 1000000007, 1315423911
            MOD2, BASE2 = 1000000009, 2654435761
            
            h1, h2 = 0, 0
            p1 = pow(BASE1, length, MOD1)
            p2 = pow(BASE2, length, MOD2)
            
            for i in range(n):
                h1 = (h1 * BASE1 + nums[i]) % MOD1
                h2 = (h2 * BASE2 + nums[i]) % MOD2
                
                if i >= length:
                    h1 = (h1 - nums[i - length] * p1) % MOD1
                    h2 = (h2 - nums[i - length] * p2) % MOD2
                    
                if i >= length - 1:
                    pair = (h1, h2)
                    if pair in seen_once:
                        seen_twice.add(pair)
                    else:
                        seen_once.add(pair)
                        
            return len(seen_once) > len(seen_twice)

        low, high = 1, n
        ans = n
        while low <= high:
            mid = (low + high) // 2
            if has_unique(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
                
        return ans
