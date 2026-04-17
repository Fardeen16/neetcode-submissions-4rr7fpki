class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        nums.sort()

        def dfs(pos, curr, total):
            if total == target:
                ans.append(curr[:])
                return
            if total > target:
                return
            prev = -1
            for i in range(pos, len(nums)):
                if nums[i] == prev:
                    continue
                curr.append(nums[i]) 
                dfs(i+1, curr, total + nums[i])
                curr.pop()
                prev = nums[i]
        
        dfs(0, [] ,0)
        return ans

