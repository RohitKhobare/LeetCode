import math

class Solution:
    def maxLength(self, nums: list[int]) -> int:
        n = len(nums)
        max_len = 1
        
        for i in range(n):
            curr_prod = 1
            curr_gcd = 0
            curr_lcm = 1
            
            for j in range(i, n):
                curr_prod *= nums[j]
                curr_gcd = math.gcd(curr_gcd, nums[j])
                curr_lcm = math.lcm(curr_lcm, nums[j])
                
                if curr_prod == curr_lcm * curr_gcd:
                    max_len = max(max_len, j - i + 1)
                    
        return max_len
