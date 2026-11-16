class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            new_s = []
            for i in range(0, len(s), k):
                group = s[i:i + k]
                group_sum = sum(int(digit) for digit in group)
                new_s.append(str(group_sum))
            s = "".join(new_s)
        return s
