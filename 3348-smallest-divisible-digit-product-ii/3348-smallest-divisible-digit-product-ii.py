from functools import lru_cache

class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        primes = [2, 3, 5, 7]
        need = []

        for p in primes:
            cnt = 0
            while t % p == 0:
                t //= p
                cnt += 1
            need.append(cnt)

        if t != 1:
            return "-1"

        fac = [
            (0, 0, 0, 0),  # 0
            (0, 0, 0, 0),  # 1
            (1, 0, 0, 0),  # 2
            (0, 1, 0, 0),  # 3
            (2, 0, 0, 0),  # 4
            (0, 0, 1, 0),  # 5
            (1, 1, 0, 0),  # 6
            (0, 0, 0, 1),  # 7
            (3, 0, 0, 0),  # 8
            (0, 2, 0, 0),  # 9
        ]

        @lru_cache(None)
        def min_digits(a, b, c, d):
            if a == b == c == d == 0:
                return 0

            ans = 10**9

            for digit in range(2, 10):
                x, y, z, w = fac[digit]

                nxt = (
                    max(0, a - x),
                    max(0, b - y),
                    max(0, c - z),
                    max(0, d - w)
                )

                if nxt != (a, b, c, d):
                    ans = min(ans, 1 + min_digits(*nxt))

            return ans

        def remaining(have):
            return tuple(max(0, need[i] - have[i]) for i in range(4))

        def build_suffix(req, length):
            req = list(req)
            result = []

            for pos in range(length):
                left = length - pos - 1

                for digit in range(1, 10):
                    f = fac[digit]

                    nxt = tuple(
                        max(0, req[i] - f[i])
                        for i in range(4)
                    )

                    if min_digits(*nxt) <= left:
                        result.append(str(digit))
                        req = list(nxt)
                        break

            return "".join(result)

        n = len(num)

        # Prime factors contributed by each valid prefix.
        prefix = [(0, 0, 0, 0)]
        first_zero = n

        for i, ch in enumerate(num):
            digit = int(ch)

            if digit == 0:
                first_zero = i
                break

            prev = prefix[-1]
            f = fac[digit]

            prefix.append(tuple(prev[j] + f[j] for j in range(4)))

        # num itself is already valid.
        if first_zero == n:
            req = remaining(prefix[-1])
            if min_digits(*req) == 0:
                return num

        # Change the rightmost possible digit to something larger,
        # then make the remaining suffix lexicographically smallest.
        last_pos = min(n - 1, first_zero)

        for i in range(last_pos, -1, -1):
            have = prefix[i]
            current = int(num[i])

            for digit in range(current + 1, 10):
                f = fac[digit]

                new_have = tuple(
                    have[j] + f[j]
                    for j in range(4)
                )

                req = remaining(new_have)
                suffix_len = n - i - 1

                if min_digits(*req) <= suffix_len:
                    return (
                        num[:i]
                        + str(digit)
                        + build_suffix(req, suffix_len)
                    )

        # No valid number of the same length.
        length = max(n + 1, min_digits(*tuple(need)))
        return build_suffix(tuple(need), length)