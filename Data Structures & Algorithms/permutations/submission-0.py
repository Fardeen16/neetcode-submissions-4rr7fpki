class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans, res = [], []
        n = len(nums)

        def backtrack():
            if len(res) == n:
                ans.append(res[:])
                return

            for num in nums:
                if num not in res:
                    res.append(num)
                    backtrack()
                    res.pop()


        backtrack()
        return ans 
        