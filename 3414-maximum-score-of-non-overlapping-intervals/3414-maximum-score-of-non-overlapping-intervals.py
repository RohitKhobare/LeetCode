class Solution:
    def maximumWeight(self, intervals):
        n = len(intervals)
        a = sorted((l, r, w, i) for i, (l, r, w) in enumerate(intervals))
        starts = [x[0] for x in a]

        from bisect import bisect_right

        nxt = [bisect_right(starts, r) for _, r, _, _ in a]

        dp = [[None] * 5 for _ in range(n + 1)]

        for k in range(5):
            dp[n][k] = (0, ())

        for i in range(n - 1, -1, -1):
            l, r, w, idx = a[i]

            for k in range(5):
                skip = dp[i + 1][k]

                if k == 4:
                    take = (-1, ())
                else:
                    ns, ids = dp[nxt[i]][k + 1]
                    take = (w + ns, tuple(sorted(ids + (idx,))))

                if take[0] > skip[0] or (take[0] == skip[0] and take[1] < skip[1]):
                    dp[i][k] = take
                else:
                    dp[i][k] = skip

        return list(dp[0][0][1])