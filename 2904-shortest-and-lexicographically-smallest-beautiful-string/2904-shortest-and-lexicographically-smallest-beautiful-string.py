class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        ones = 0
        left = 0
        best = ""

        for right in range(len(s)):
            if s[right] == '1':
                ones += 1

            while ones > k:
                if s[left] == '1':
                    ones -= 1
                left += 1

            if ones == k:
                while s[left] == '0':
                    left += 1

                cur = s[left:right + 1]

                if not best or len(cur) < len(best) or (
                    len(cur) == len(best) and cur < best
                ):
                    best = cur

        return best