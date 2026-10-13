class Solution:
    def maxAlternatingSum(self, nums: list[int]) -> int:
        squares = sorted((x * x for x in nums), reverse=True)
        half = (len(nums) + 1) // 2
        return sum(squares[:half]) - sum(squares[half:])