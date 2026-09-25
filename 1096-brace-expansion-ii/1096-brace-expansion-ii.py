class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        self.s = expression
        self.i = 0

        def parse_expr():
            res = parse_concat()

            while self.i < len(self.s) and self.s[self.i] == ',':
                self.i += 1
                res |= parse_concat()

            return res

        def parse_concat():
            res = {""}

            while self.i < len(self.s) and self.s[self.i] not in ',}':
                if self.s[self.i] == '{':
                    self.i += 1
                    cur = parse_expr()
                    self.i += 1
                else:
                    cur = {self.s[self.i]}
                    self.i += 1

                res = {a + b for a in res for b in cur}

            return res

        return sorted(parse_expr())