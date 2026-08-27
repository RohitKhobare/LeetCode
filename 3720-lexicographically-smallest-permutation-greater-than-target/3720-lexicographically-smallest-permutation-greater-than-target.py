class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        cnt = [0] * 26
        for c in s:
            cnt[ord(c) - ord('a')] += 1

        n = len(s)

        def build(cnt, prefix):
            res = prefix
            for i in range(26):
                if cnt[i]:
                    cnt[i] -= 1
                    res += chr(i + ord('a'))
                    res += ''.join(
                        chr(j + ord('a')) * cnt[j]
                        for j in range(26)
                    )
                    return res
            return res

        # Try matching target as long as possible.
        for i in range(n - 1, -1, -1):
            cnt2 = cnt[:]

            # Use target[0:i] exactly.
            possible = True
            for j in range(i):
                x = ord(target[j]) - ord('a')
                if cnt2[x] == 0:
                    possible = False
                    break
                cnt2[x] -= 1

            if not possible:
                continue

            # At position i, choose smallest char > target[i].
            t = ord(target[i]) - ord('a')

            for c in range(t + 1, 26):
                if cnt2[c] > 0:
                    cnt2[c] -= 1

                    ans = target[:i] + chr(c + ord('a'))
                    ans += ''.join(
                        chr(j + ord('a')) * cnt2[j]
                        for j in range(26)
                    )
                    return ans

        return ""