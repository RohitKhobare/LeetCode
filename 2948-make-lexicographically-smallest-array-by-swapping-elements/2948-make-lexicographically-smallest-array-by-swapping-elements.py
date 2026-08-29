class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        arr = sorted((num, i) for i, num in enumerate(nums))
        ans = nums[:]

        start = 0

        for end in range(1, len(arr) + 1):
            if end == len(arr) or arr[end][0] - arr[end - 1][0] > limit:
                values = sorted(arr[start:end], key=lambda x: x[1])
                nums_sorted = sorted(x[0] for x in arr[start:end])

                for j, (_, idx) in enumerate(values):
                    ans[idx] = nums_sorted[j]

                start = end

        return ans