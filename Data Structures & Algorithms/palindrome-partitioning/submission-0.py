class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans, res = [], []
        n = len(s)

        def isPalin(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l, r = l + 1, r - 1
            return True

        def backtrack(index):
            if index == n:
                ans.append(res[:])
                return

            for j in range(index, n):
                if isPalin(index, j):
                    res.append(s[index: j + 1])
                    backtrack(j+ 1)
                    res.pop()

        backtrack(0)
        return ans



        