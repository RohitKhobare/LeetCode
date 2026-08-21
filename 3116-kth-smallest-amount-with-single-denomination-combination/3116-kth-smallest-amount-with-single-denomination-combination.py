from typing import List
from math import gcd


class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        n = len(coins)

        def lcm(a, b):
            return a // gcd(a, b) * b

        def count(x):
            total = 0

            for mask in range(1, 1 << n):
                value = 1
                bits = 0

                for i in range(n):
                    if mask & (1 << i):
                        value = lcm(value, coins[i])
                        bits += 1

                        if value > x:
                            break

                else:
                    cur = x // value

                    if bits % 2:
                        total += cur
                    else:
                        total -= cur

            return total

        left = 1
        right = min(coins) * k

        while left < right:
            mid = (left + right) // 2

            if count(mid) >= k:
                right = mid
            else:
                left = mid + 1

        return left