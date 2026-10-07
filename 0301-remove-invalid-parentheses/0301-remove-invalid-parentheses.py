class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        left = right = 0

        for ch in s:
            if ch == '(':
                left += 1
            elif ch == ')':
                if left > 0:
                    left -= 1
                else:
                    right += 1

        result = set()

        def backtrack(i, path, balance, l_remove, r_remove):
            if i == len(s):
                if balance == 0 and l_remove == 0 and r_remove == 0:
                    result.add(''.join(path))
                return

            ch = s[i]

            if ch == '(':
                # Remove this '('
                if l_remove > 0:
                    backtrack(i + 1, path, balance, l_remove - 1, r_remove)

                # Keep this '('
                path.append(ch)
                backtrack(i + 1, path, balance + 1, l_remove, r_remove)
                path.pop()

            elif ch == ')':
                # Remove this ')'
                if r_remove > 0:
                    backtrack(i + 1, path, balance, l_remove, r_remove - 1)

                # Keep this ')' only if it can be matched
                if balance > 0:
                    path.append(ch)
                    backtrack(i + 1, path, balance - 1, l_remove, r_remove)
                    path.pop()

            else:
                path.append(ch)
                backtrack(i + 1, path, balance, l_remove, r_remove)
                path.pop()

        backtrack(0, [], 0, left, right)
        return list(result)