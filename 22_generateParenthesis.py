# Given n pairs of parentheses, write a function to generate all combinations
# of well-formed parentheses.

# Input: n = 3
# Output: ["((()))", "(()())", "(())()", "()(())", "()()()"]

from typing import List

# DFS solution


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        stack = []
        res = []

        def backtrack(openN, closedN):
            if openN == closedN == n:
                # ending case
                res.append(''.join(stack))
                return

            if openN < n:
                stack.append('(')
                backtrack(openN+1, closedN)
                stack.pop()

            if closedN < openN:
                stack.append(')')
                backtrack(openN, closedN+1)
                stack.pop()

        backtrack(0, 0)
        return res


ans = Solution().generateParenthesis(3)
print(ans)
