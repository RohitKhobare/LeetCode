from typing import List


class Solution:
    def remainingMethods(
        self,
        n: int,
        k: int,
        invocations: List[List[int]]
    ) -> List[int]:
        graph = [[] for _ in range(n)]

        for caller, called in invocations:
            graph[caller].append(called)

        suspicious = set()
        stack = [k]

        while stack:
            method = stack.pop()

            if method in suspicious:
                continue

            suspicious.add(method)

            for called in graph[method]:
                stack.append(called)

        for caller, called in invocations:
            if caller not in suspicious and called in suspicious:
                return list(range(n))

        return [method for method in range(n) if method not in suspicious]