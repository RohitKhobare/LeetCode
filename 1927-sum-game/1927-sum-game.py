class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num) // 2

        left_sum = 0
        right_sum = 0
        left_q = 0
        right_q = 0

        for i in range(n):
            if num[i] == '?':
                left_q += 1
            else:
                left_sum += int(num[i])

        for i in range(n, 2 * n):
            if num[i] == '?':
                right_q += 1
            else:
                right_sum += int(num[i])

        diff = left_sum - right_sum
        q_diff = left_q - right_q

        if q_diff % 2 != 0:
            return True

        return diff != -(q_diff // 2) * 9