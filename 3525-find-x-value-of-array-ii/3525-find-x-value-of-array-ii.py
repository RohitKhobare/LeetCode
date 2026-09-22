class Solution:
    def resultArray(self, nums, k, queries):
        n = len(nums)
        size = 1

        while size < n:
            size <<= 1

        tree = [(1 % k, [0] * k) for _ in range(2 * size)]

        for i in range(n):
            r = nums[i] % k
            cnt = [0] * k
            cnt[r] = 1
            tree[size + i] = (r, cnt)

        def merge(a, b):
            pa, ca = a
            pb, cb = b

            p = (pa * pb) % k
            cnt = ca[:]

            for r in range(k):
                cnt[(pa * r) % k] += cb[r]

            return p, cnt

        for i in range(size - 1, 0, -1):
            tree[i] = merge(tree[i << 1], tree[i << 1 | 1])

        def update(pos, val):
            p = size + pos
            r = val % k
            cnt = [0] * k
            cnt[r] = 1
            tree[p] = (r, cnt)

            p >>= 1
            while p:
                tree[p] = merge(tree[p << 1], tree[p << 1 | 1])
                p >>= 1

        def query(l, r):
            left = None
            right = None

            l += size
            r += size

            while l <= r:
                if l & 1:
                    left = tree[l] if left is None else merge(left, tree[l])
                    l += 1

                if not (r & 1):
                    right = tree[r] if right is None else merge(tree[r], right)
                    r -= 1

                l >>= 1
                r >>= 1

            if left is None:
                return right
            if right is None:
                return left

            return merge(left, right)

        result = []

        for index, value, start, x in queries:
            update(index, value)
            result.append(query(start, n - 1)[1][x])

        return result