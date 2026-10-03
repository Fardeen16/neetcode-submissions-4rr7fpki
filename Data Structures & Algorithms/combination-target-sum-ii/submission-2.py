class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        n = len(nums)
        nums.sort()

        def backtrack(index, arr, total):
            if total == target:
                ans.append(arr[:])
                return
            
            if total > target or index == n:
                return

            #choose current numbeer
            arr.append(nums[index])
            backtrack(index+1, arr, total + nums[index])
            arr.pop()

             #choose the next index
            while index+1 < n and nums[index] == nums[index+1]:
                index += 1
            backtrack(index+1, arr, total)

        backtrack(0, [], 0)
        return ans