from typing import List

class Solution:
    def minMoves(self, nums: List[int]) -> int:
        minimum = min(nums)
        return sum(nums) - len(nums) * minimum