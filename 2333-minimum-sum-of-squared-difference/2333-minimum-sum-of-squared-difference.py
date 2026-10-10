class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        diffs = [abs(a - b) for a, b in zip(nums1, nums2)]
        k = k1 + k2

        if sum(diffs) <= k:
            return 0

        diffs.sort(reverse=True)

        for i in range(len(diffs)):
            if i == len(diffs) - 1 or diffs[i] > diffs[i + 1]:
                needed = (diffs[i] - (diffs[i + 1] if i + 1 < len(diffs) else 0)) * (i + 1)

                if k >= needed:
                    k -= needed
                    continue

                level, rem = divmod(k, i + 1)
                target = diffs[i] - level

                return sum(d * d for d in diffs[i + 1:]) + (i + 1 - rem) * target * target + rem * (target - 1) * (target - 1)

        return sum(d * d for d in diffs)