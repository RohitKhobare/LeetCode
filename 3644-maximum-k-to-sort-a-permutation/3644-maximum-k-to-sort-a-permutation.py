from typing import List

class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        k = -1

        for i, x in enumerate(nums):
            if i != x:
                k &= x

        return max(k, 0)
        