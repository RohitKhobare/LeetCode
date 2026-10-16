from typing import List

class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        size = 4 * n
        sum_tree = [0] * size
        sq_tree = [0] * size
        lazy = [0] * size
        last = {}
        ans = 0

        def apply(node, l, r, val):
            length = r - l + 1
            old_sum = sum_tree[node]
            sq_tree[node] = (sq_tree[node] + 2 * val * old_sum + val * val * length) % MOD
            sum_tree[node] = (old_sum + val * length) % MOD
            lazy[node] += val

        def push(node, l, r):
            if lazy[node] == 0 or l == r:
                return
            mid = (l + r) // 2
            val = lazy[node]
            apply(node * 2, l, mid, val)
            apply(node * 2 + 1, mid + 1, r, val)
            lazy[node] = 0

        def update(node, l, r, ql, qr, val):
            if ql <= l and r <= qr:
                apply(node, l, r, val)
                return

            push(node, l, r)
            mid = (l + r) // 2

            if ql <= mid:
                update(node * 2, l, mid, ql, qr, val)
            if qr > mid:
                update(node * 2 + 1, mid + 1, r, ql, qr, val)

            sum_tree[node] = (sum_tree[node * 2] + sum_tree[node * 2 + 1]) % MOD
            sq_tree[node] = (sq_tree[node * 2] + sq_tree[node * 2 + 1]) % MOD

        for i, x in enumerate(nums):
            p = last.get(x, -1) + 1
            update(1, 0, n - 1, p, i, 1)
            ans = (ans + sq_tree[1]) % MOD
            last[x] = i

        return ans