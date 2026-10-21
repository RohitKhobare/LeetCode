class Solution:
    def minOperations(self, s: str) -> int:
        if s == ''.join(sorted(s)):
            return 0

        n = len(s)

        if n == 2:
            return -1

        smallest = min(s)
        largest = max(s)

        if s[0] == largest and s[-1] == smallest:
            if n == 3:
                return 2 if s[1] == smallest or s[1] == largest else 3
            if s.count(largest) > 1 or s.count(smallest) > 1:
                return 2
            return 3

        if s[0] == smallest or s[-1] == largest:
            return 1

        return 2