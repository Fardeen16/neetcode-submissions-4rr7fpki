class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        curMin, curMax = 1, 1

        for n in nums:
            tmp = curMax * n
            curMax = max(n * curMin, n * curMax, n)
            curMin = min(n * curMin, tmp, n)
            res = max(curMax, res)

        return res
        