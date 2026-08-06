from typing import List

class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return 0

        mn = min(nums)
        mx = max(nums)

        if mn == mx:
            return 0

        bucket_size = max(1, (mx - mn) // (n - 1))
        bucket_count = (mx - mn) // bucket_size + 1

        buckets = [[float('inf'), float('-inf')] for _ in range(bucket_count)]

        for num in nums:
            idx = (num - mn) // bucket_size
            buckets[idx][0] = min(buckets[idx][0], num)
            buckets[idx][1] = max(buckets[idx][1], num)

        ans = 0
        prev_max = mn

        for bmin, bmax in buckets:
            if bmin == float('inf'):
                continue
            ans = max(ans, bmin - prev_max)
            prev_max = bmax

        return ans