class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans, res = [], []

        def backtrack(left_b, right_b):
            if len(res) == 2*n:
                ans.append("".join(res))
                return

            if left_b < n:
                res.append("(")
                backtrack(left_b + 1, right_b)
                res.pop()

            if left_b > right_b:
                res.append(")")
                backtrack(left_b, right_b + 1)
                res.pop()

        backtrack(0, 0)
        return ans