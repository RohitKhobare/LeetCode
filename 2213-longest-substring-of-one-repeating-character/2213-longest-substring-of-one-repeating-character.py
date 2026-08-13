class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        n = len(s)
        s = list(s)

        pref = [0] * (4 * n)
        suff = [0] * (4 * n)
        best = [0] * (4 * n)
        length = [0] * (4 * n)
        leftChar = [''] * (4 * n)
        rightChar = [''] * (4 * n)

        def merge(node):
            l = node * 2
            r = l + 1

            length[node] = length[l] + length[r]
            leftChar[node] = leftChar[l]
            rightChar[node] = rightChar[r]

            pref[node] = pref[l]
            suff[node] = suff[r]
            best[node] = max(best[l], best[r])

            if rightChar[l] == leftChar[r]:
                best[node] = max(best[node], suff[l] + pref[r])

                if pref[l] == length[l]:
                    pref[node] = length[l] + pref[r]

                if suff[r] == length[r]:
                    suff[node] = length[r] + suff[l]

        def build(node, lo, hi):
            if lo == hi:
                pref[node] = suff[node] = best[node] = length[node] = 1
                leftChar[node] = rightChar[node] = s[lo]
                return

            mid = (lo + hi) // 2
            build(node * 2, lo, mid)
            build(node * 2 + 1, mid + 1, hi)
            merge(node)

        def update(node, lo, hi, idx, ch):
            if lo == hi:
                leftChar[node] = rightChar[node] = ch
                return

            mid = (lo + hi) // 2

            if idx <= mid:
                update(node * 2, lo, mid, idx, ch)
            else:
                update(node * 2 + 1, mid + 1, hi, idx, ch)

            merge(node)

        build(1, 0, n - 1)

        ans = []

        for idx, ch in zip(queryIndices, queryCharacters):
            s[idx] = ch
            update(1, 0, n - 1, idx, ch)
            ans.append(best[1])

        return ans