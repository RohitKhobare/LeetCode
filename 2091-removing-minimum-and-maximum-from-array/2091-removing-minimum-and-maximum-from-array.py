class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)

        min_idx = nums.index(min(nums))
        max_idx = nums.index(max(nums))

        left = min(min_idx, max_idx)
        right = max(min_idx, max_idx)

        # Both from front
        front = right + 1

        # Both from back
        back = n - left

        # min from front, max from back
        mixed = (left + 1) + (n - right)

        return min(front, back, mixed)