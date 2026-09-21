class Solution:
    def resultArray(self, nums, k):
        dp = [0] * k
        ans = [0] * k

        for num in nums:
            r = num % k
            new = [0] * k
            new[r] += 1

            for j in range(k):
                new[(j * r) % k] += dp[j]

            dp = new

            for j in range(k):
                ans[j] += dp[j]

        return ans