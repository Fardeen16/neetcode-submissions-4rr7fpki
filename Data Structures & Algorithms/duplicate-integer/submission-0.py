class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        ans = set()

        for i in nums:
            if i in ans:
                return True
            else:
                ans.add(i)
        return False