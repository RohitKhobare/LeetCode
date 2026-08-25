class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        nums = set(nums)

        multiple = k

        while multiple in nums:
            multiple += k

        return multiple