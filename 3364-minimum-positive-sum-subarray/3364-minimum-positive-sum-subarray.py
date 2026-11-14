class Solution:
    def minimumSumSubarray(self, nums: list[int], l: int, r: int) -> int:
        n = len(nums)
        min_sum = float('inf')
        
        for i in range(n):
            curr_sum = 0
            for j in range(i, min(n, i + r)):
                curr_sum += nums[j]
                if j - i + 1 >= l and curr_sum > 0:
                    min_sum = min(min_sum, curr_sum)
                    
        return min_sum if min_sum != float('inf') else -1
