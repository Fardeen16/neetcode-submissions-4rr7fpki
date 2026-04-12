class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans, res = [], []
        n = len(nums)
        nums.sort()

        def backtrack(i):
            if i == n:
                ans.append(res[:])
                return

            res.append(nums[i])
            backtrack(i+1)
            res.pop()

            while i+1 < n and nums[i] == nums[i+1]:
                i += 1
            backtrack(i+1)
            

        backtrack(0)
        return ans
        